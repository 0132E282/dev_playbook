#!/usr/bin/env python3
import subprocess
import sys
import time
import os
import argparse
import json
from shutil import which

class TestRunner:
    def __init__(self):
        self.stats = {"passed": 0, "failed": 0, "skipped": 0, "total": 0}
        self.results = []
        self.start_time = time.time()

    def log(self, message, emoji="ℹ️"):
        print(f"{emoji} {message}")

    def run_command(self, command, description, cwd=None):
        print(f"\n🚀 Running: {description}...")
        print(f"   Command: {command}")

        cmd_start = time.time()
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            duration = time.time() - cmd_start

            output_lines = result.stdout.strip().split('\n') if result.stdout else []
            error_lines = result.stderr.strip().split('\n') if result.stderr else []

            status = "PASSED" if result.returncode == 0 else "FAILED"

            if result.returncode == 0:
                print(f"✅ Success ({duration:.2f}s)")
                for line in output_lines[-5:]:
                    print(f"   | {line}")
            else:
                print(f"❌ Failed ({duration:.2f}s)")
                print("   Error Output:")
                display_lines = error_lines[-20:] if error_lines else output_lines[-20:]
                for line in display_lines:
                    print(f"   | {line}")

            self.results.append({
                "name": description,
                "command": command,
                "status": status,
                "duration": duration,
                "error": "\n".join(error_lines[-5:]) if status == "FAILED" else ""
            })

            return result.returncode == 0

        except Exception as e:
            print(f"❌ Exception: {str(e)}")
            self.results.append({
                "name": description,
                "command": command,
                "status": "ERROR",
                "duration": 0,
                "error": str(e)
            })
            return False

    def detect_and_run(self, mode="all"):
        self.log("Detecting project environment...", "🔍")

        # 1. PHP / Laravel
        if os.path.exists("composer.json"):
            self.handle_php(mode)

        # 2. Node.js / React / Express / NestJS
        if os.path.exists("package.json"):
            self.handle_node_react(mode)

        # 3. ASP.NET / C# (Check root and 1-level deep)
        if self._detect_dotnet():
            self.handle_dotnet(mode)

        # 4. Python
        if os.path.exists("requirements.txt") or os.path.exists("pyproject.toml"):
            self.handle_python(mode)

    def handle_php(self, mode):
        if mode in ["unit", "all"]:
            if os.path.exists("artisan"):
                if os.path.exists("tests"):
                    self.execute("php artisan test", "Laravel Artisan Test")
                else:
                    self.skip("Laravel Artisan Test", "Thư mục 'tests' không tồn tại")
            elif os.path.exists("vendor/bin/pest"):
                self.execute("vendor/bin/pest --parallel", "Pest PHP")
            elif os.path.exists("vendor/bin/phpunit"):
                if os.path.exists("tests"):
                    self.execute("vendor/bin/phpunit", "PHPUnit")
                else:
                    self.skip("PHPUnit", "Thư mục 'tests' không tồn tại")

    def handle_node_react(self, mode):
        with open("package.json") as f:
            pkg = json.load(f)
            scripts = pkg.get("scripts", {})
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

        is_react = "react" in deps
        label_prefix = "React" if is_react else "Node.js"

        if mode in ["unit", "all"]:
            if "test" in scripts and scripts["test"] != 'echo "Error: no test specified" && exit 1':
                self.execute("npm test", f"{label_prefix} NPM Test")
            elif "test:unit" in scripts:
                self.execute("npm run test:unit", f"{label_prefix} Unit Test")
            elif "vitest" in deps:
                self.execute("npx vitest run", f"{label_prefix} Vitest")
            elif "jest" in deps:
                self.execute("npx jest", f"{label_prefix} Jest")
            else:
                self.skip(f"{label_prefix} Unit Test", "Không tìm thấy script 'test' hoặc test runner (Jest/Vitest) trong package.json")

        if mode in ["e2e", "all"]:
            if os.path.exists("playwright.config.ts") or os.path.exists("playwright.config.js"):
                 self.execute("npx playwright test", f"{label_prefix} Playwright E2E")
            elif "test:e2e" in scripts:
                self.execute("npm run test:e2e", f"{label_prefix} E2E Test")
            elif "cypress" in deps:
                 self.execute("npx cypress run", f"{label_prefix} Cypress E2E")

    def handle_dotnet(self, mode):
        if mode in ["unit", "all"]:
            if which("dotnet"):
                self.execute("dotnet test", "ASP.NET / .NET Core Test")
            else:
                self.skip("ASP.NET Test", "dotnet SDK chưa được cài đặt")

    def handle_python(self, mode):
        if mode in ["unit", "all"]:
            if os.path.exists("pytest.ini") or which("pytest"):
                self.execute("pytest", "Pytest (Python)")
            else:
                self.execute("python3 -m unittest discover", "Python Unittest")

    def execute(self, cmd, label):
        self.stats["total"] += 1
        if self.run_command(cmd, label):
            self.stats["passed"] += 1
        else:
            self.stats["failed"] += 1

    def skip(self, label, reason):
        self.stats["total"] += 1
        self.stats["skipped"] += 1
        self.results.append({
            "name": label,
            "status": "SKIPPED",
            "duration": 0,
            "error": reason
        })
        self.log(f"Skipped {label}: {reason}", "⏭️")

    def _detect_dotnet(self):
        # Check root
        if any(f.endswith(".sln") or f.endswith(".csproj") for f in os.listdir(".")):
            return True
        # Check subdirectories (1 level deep)
        for d in os.listdir("."):
            if os.path.isdir(d) and not d.startswith("."):
                try:
                    if any(f.endswith(".sln") or f.endswith(".csproj") for f in os.listdir(d)):
                        return True
                except PermissionError:
                    continue
        return False

    def report(self):
        duration = time.time() - self.start_time
        print("\n" + "="*70)
        print(f"📊 AUTOMATED TEST SUMMARY ({duration:.2f}s)")
        print("="*70)

        if not self.results:
            print("⚠️  Không tìm thấy test nào để chạy.")
            print("   Vui lòng kiểm tra lại cấu trúc thư mục hoặc file cấu hình (composer.json, package.json, .sln, etc).")
        else:
            print(f"{'KẾT QUẢ':<10} | {'BỘ TEST (SUITE)':<35} | {'THỜI GIAN'}")
            print("-" * 70)
            for res in self.results:
                if res["status"] == "PASSED":
                    icon, color = "✅", "\033[92m"
                elif res["status"] == "FAILED":
                    icon, color = "❌", "\033[91m"
                elif res["status"] == "SKIPPED":
                    icon, color = "⏭️ ", "\033[93m"
                else:
                    icon, color = "❓", "\033[0m"

                reset = "\033[0m"
                print(f"{icon} {res['status']:<7} | {res['name']:<35} | {res['duration']:.2f}s")
                if res["status"] == "FAILED":
                    print(f"   └─ Lỗi: {res['error'].strip()[:100]}...")
                elif res["status"] == "SKIPPED":
                    print(f"   └─ Lý do: {res['error']}")

            print("-" * 70)
            print(f"Tổng cộng: {self.stats['total']} | Thành công: {self.stats['passed']} | Thất bại: {self.stats['failed']} | Bỏ qua: {self.stats['skipped']}")

        return self.stats["failed"] == 0

def main():
    parser = argparse.ArgumentParser(description="Clean Testing Auto-Runner for PHP, Node, React, ASP.NET, Python")
    parser.add_argument("--mode", choices=["all", "unit", "e2e"], default="all", help="Chế độ chạy test (mặc định: all)")
    args = parser.parse_args()

    runner = TestRunner()
    runner.detect_and_run(args.mode)
    success = runner.report()

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
