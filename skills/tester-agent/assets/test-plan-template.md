# Test Plan / Strategy Template

**Feature**: [Tên tính năng]
**Owner**: [Người phụ trách]
**Date**: [Ngày tạo]

---

## 1. Scope (Phạm vi)
*   **In-Scope**: Những gì sẽ test? (Ví dụ: Flow đăng ký, validate form, gửi mail confirmation).
*   **Out-Scope**: Những gì KHÔNG test? (Ví dụ: UX visual, tích hợp bên thứ 3 environment chết).

## 2. Test Scenarios (Ma trận kiểm thử)

| ID | Test Scenario | Type | Data Setup | Expected Result | Priority |
|----|---------------|------|------------|-----------------|----------|
| 01 | Đăng ký thành công | Valid | Email chưa tồn tại | User được tạo, status=active, nhận mail | P0 (Critical) |
| 02 | Email trùng lặp | Invalid | Email đã tồn tại | Lỗi 422 "Email already exists" | P1 |
| 03 | Password quá ngắn | Boundary | Pass = 5 ký tự | Lỗi Validation | P2 |
| 04 | SQL Injection ở tên | Security | Name = `' OR 1=1 --` | Hệ thống sanitize, tạo user với tên đó | P1 |
| 05 | Spam click submit | Performance | Network delay | Chỉ 1 request được xử lý | P2 |

## 3. Test Pyramid Strategy

### Unit Tests (Backend/Frontend logic)
*   [ ] Validate input rules.
*   [ ] Logic tính toán (nếu có).
*   [ ] Exception handling (DB down, API timeout).

### Integration Tests (Database/API)
*   [ ] Query DB tạo user đúng chưa?
*   [ ] API trả về đúng JSON format không?

### E2E Tests (Luồng người dùng)
*   [ ] User vào trang -> Điền form -> Submit -> Thấy thông báo thành công.

## 4. Risks & Mitigations
*   **Risk**: Email server test bị giới hạn rate limit.
*   **Mitigation**: Dùng mail driver `log` hoặc `array` để mock việc gửi mail.
