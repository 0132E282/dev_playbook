# Hướng Dẫn Security Audit

Tài liệu này cung cấp các nguyên tắc chuyên sâu để thực hiện Security Audit theo mẫu `security-audit-template.md`.

## 1. Kiểm soát đầu vào (Input Validation)
- **Trust No One**: Tất cả dữ liệu từ bên ngoài (API params, query strings, headers, file uploads) đều phải được coi là không an toàn.
- **Whitelist over Blacklist**: Ưu tiên kiểm tra các ký tự/mẫu được cho phép thay vì cố gắng loại bỏ các ký tự xấu.
- **Ràng buộc dữ liệu**: Kiểm tra kiểu dữ liệu, độ dài tối đa và bộ lọc hợp lệ ngay tại tầng Controller/DTO.

## 2. Các lỗi Tiêm nhiễm (Injection Flaws)
- **SQL Injection**: Tuyệt đối không cộng chuỗi để tạo query. Luôn sử dụng Parameterized Queries hoặc LINQ/ORM (EF Core) đã được bảo mật.
- **XSS (Cross-Site Scripting)**: Escaping tất cả nội dung do người dùng tạo ra trước khi render. Trong C#/.NET, hãy cẩn thận với `Html.Raw` hoặc các thuộc tính gán trực tiếp vào HTML.
- **Command Injection**: Không sử dụng các hàm hệ thống (`Process.Start`, `exec`) với tham số từ người dùng mà chưa qua kiểm duyệt nghiêm ngặt.

## 3. Xác thực & Phân quyền (Auth & Access Control)
- **Broken Access Control (IDOR)**: Luôn xác minh người dùng hiện tại có thực sự sở hữu hoặc có quyền truy cập vào Resource tương ứng (đọc/sửa/xóa) thông qua ID. Không tin cậy mù quáng vào ID gửi lên từ URL.
- **Least Privilege**: Tài khoản database của ứng dụng chỉ nên có quyền tối thiểu cần thiết để hoạt động.
- **RBAC/ABAC**: Đảm bảo Middleware hoặc Attribute `[Authorize(Permissions = ...)]` được áp dụng đúng vị trí.

## 4. Bảo vệ dữ liệu nhạy cảm (Sensitive Data)
- **Không Hardcode Secrets**: Sử dụng `User Secrets` (khi dev) hoặc `Environment Variables`, `Key Vault` (khi prod).
- **Hạn chế lộ dữ liệu**: Không bao giờ trả về toàn bộ Model (chứa PasswordHash, Info nhạy cảm) trong API response. Luôn sử dụng DTO/Resource Filter.
- **Logging**: Tuyệt đối không ghi log mật khẩu, thông tin thẻ tín dụng hoặc PII (Personally Identifiable Information).

---

## 5. Mapping ISSUE vào Security Audit Template

| Hạng mục | Template Key | Hành động khi phát hiện |
| :--- | :--- | :--- |
| **Lỗi SQL/XSS** | `1. Injection Flaws` | Đưa vào danh sách **Critical Findings**. |
| **Lỗi IDOR** | `2. Auth & Auth` | Đánh dấu `!` Critical nếu user có thể sửa data người khác. |
| **Lộ Secrets** | `3. Data Protection` | Yêu cầu thu hồi key cũ và thay bằng Env Var. |
| **Thiếu Validation** | `4. Input Validation` | Đánh dấu `?` Warning nếu thiếu logic kiểm tra độ dài. |

---

## 6. Checklist Audit Nhanh

- [ ] Bạn đã thử thay đổi ID trong URL để truy cập data người khác chưa?
- [ ] Tham số đầu vào có thể chứa code `<script>` hoặc `' OR 1=1` không?
- [ ] Các thông tin nhạy cảm có được mã hóa khi lưu trữ và truyền tải không?
- [ ] Log hệ thống có chứa thông tin định danh cá nhân (PII) không?
