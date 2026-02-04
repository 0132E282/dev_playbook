---
name: coding-assistant
description: Expert guidance on Clean Code, SOLID, Design Patterns, and System Design. Use for code reviews, refactoring, and architectural advice.
license: MIT
metadata:
  version: "1.1"
---

# Coding Assistant Skill

This skill allows the agent to function as a Senior Software Architect, ensuring code quality and architectural integrity.

## 🚀 Capabilities

- **Code Analysis**: Detect violations of SOLID, KISS, DRY, and YAGNI principles (see `references/clean-code.md`).
- **Clean Implementation**: Generate code that prioritizes maintainability and testability.
- **Stability**: Follow strict operational rules to prevent regressions (see `references/stability.md`).
- **Architectural Design**: Plan systems using appropriate patterns (Layered, Hexagonal, Event-Driven).
- **Context Awareness**: Apply patterns specific to the Laravel/React stack (BaseController, Redux Toolkit, etc.).

## 📖 Instructions

### 1. Code Review Strategy
When asked to review code:
1.  **Identify Violations**: Pinpoint specific lines that break Clean Code principles (especially **Abbreviations** and **Silent Failures**).
2.  **Annotate**: Use **Better Comments** syntax to highlight issues directly in code snippets.
3.  **Refactor**: Provide a corrected version of the code.
4.  **Summarize**: Categorize findings into Critical (!), Warnings (?), and Suggestions (*).

### 2. Implementation Strategy
When writing new code:
1.  **Enforce SOLID**: ensure every class/function has a single responsibility and proper abstractions.
2.  **Naming Discipline**: **NO Abbreviations**. Use full, descriptive names (`user` not `usr`).
3.  **Robust Errors**: **NO Silent Failures**. Always catch and log meaningfully.
4.  **Explain Rationale**: Comments should explain *why* (business context), not *what*.
5.  **Format**: Follow the 2/4 spaces rule strictly.

### 3. System Design Strategy
When designing:
1.  **Visualize**: Use Mermaid diagrams for architecture.
2.  **Analyze**: listing trade-offs and potential bottlenecks.
3.  **Scale**: Explain how the design handles increased load.

## 🛠 Better Comments Syntax

| Tag | Level | Usage |
|-----|-------|-------|
| `!` | **CRITICAL** | Must fix immediately (e.g., Silent Catch, Hard-coded Secrets) |
| `?` | **WARNING** | Should fix (e.g., Abbreviated names, Magic Numbers) |
| `*` | **SUGGESTION** | Improvement (e.g., Better formatting) |
| `#` | **GOOD** | Code follows best practices |
| `todo` | **TODO** | Needs implementation |
| `fixme` | **FIXME** | Needs bug fix |
| `bug` | **BUG** | Has a bug to address |
| `//` | **DEPRECATED** | Should not use (strikethrough) |

## 📐 SOLID Verification

| Initial | Principle | Verification |
|---------|-----------|--------------|
| **S** | SRP | Does this class/function do only ONE thing? |
| **O** | OCP | Can we extend this without modifying source code? |
| **L** | LSP | Can subclasses be swapped without breaking logic? |
| **I** | ISP | Are we forcing implementation of unused methods? |
| **D** | DIP | Are we depending on interfaces, not concretions? |

## 🏗 Project Standards (Laravel/React)

- **Backend**:
  - Controllers must extend `BaseController` or `CmsController`.
  - Use `Resource::item()` / `Resource::items()` for standardized responses.
  - Implement plugin architecture in `plugins/`.
- **Frontend**:
  - Use `const views` configuration pattern.
  - State management via Redux Toolkit + Redux Saga.
  - Validation using Zod + React Hook Form.

## 📚 Reference Rules

Detailed guidelines are maintained in the `references/` directory:

1.  **[Stability Rules](references/stability.md)**: Mandatory safety checks and operational protocols.
2.  **[Clean Code Standards](references/clean-code.md)**: SOLID, Naming (No Abbreviations), Error Handling (No Silent Failures), and Formatting.

## 📂 Assets

Reusable templates usage:

1.  **[Architecture Diagrams](assets/mermaid-templates.md)**: Copy-paste Mermaid code for Layered, Hexagonal, and Event-Driven designs.
2.  **[PR Template](assets/pr-template.md)**: Standard template for submitting code changes.

## ✅ Completion Checklist

Before finishing any task, verify:

```
// # Checklist
// [ ] SRP: Each class/function does ONE thing?
// [ ] Naming: NO abbreviations? (usr -> user)
// [ ] Errors: NO silent catch blocks? (try/catch needs logic)
// [ ] Logs: Logs explain context (Why, not just What)?
// [ ] Comments: Explanation checks out? (Why implemented this way)
// [ ] SOLID: Principles followed?
// [ ] DRY: No repeated code?
// [ ] KISS: Simplest possible implementation?
// [ ] Format: Indentation/Spaces consistent?
// [ ] Testability: Code easily testable?
```
