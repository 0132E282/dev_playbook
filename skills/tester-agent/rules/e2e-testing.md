# E2E Testing Rules (Playwright / Cypress)

E2E Test giả lập hành vi thực tế của người dùng trên trình duyệt (Click, Type, Navigation).

## 1. Ưu tiên Locators chịu lỗi (Resilient Locators)
*   **Tránh dùng XPath hoặc CSS selector** gắn liền với cấu trúc DOM (e.g. `div > div > button`).
*   **Nên dùng**:
    *   `getByRole('button', { name: 'Submit' })`
    *   `getByLabel('Email')`
    *   `getByPlaceholder('Nhập mật khẩu')`
    *   `getByTestId('login-btn')` (Nếu các locator trên không khả dụng).

## 2. Page Object Model (POM)
*   Đóng gói logic tương tác của một trang vào một Class.
*   Giúp bảo trì dễ dàng: Khi UI thay đổi button login, bạn chỉ cần sửa 1 chỗ trong class POM thay vì sửa 100 file test.

## 3. Chống Flakiness (Test chạy lúc pass lúc fail)
*   **KHÔNG dùng Hard Waits**: Tuyệt đối không dùng `sleep(5000)`.
*   **Nên dùng Auto-waiting**: Playwright tự động đợi element sẵn sàng trước khi click. Hoặc dùng `webFirst` assertions: `await expect(locator).toBeVisible()`.

## 4. Reset State cho mỗi Test
*   Mỗi test nên bắt đầu bằng việc Login (nếu cần) hoặc xóa Cookies/Storage để không bị ảnh hưởng bởi session trước.
*   Nên có các Script setup DB nhanh cho E2E để có dữ liệu khởi đầu.

## 5. Chụp ảnh & Quay video khi lỗi
*   Cấu hình công cụ để tự động chụp screenshot hoặc quay video khi test FAILED. Điều này cực kỳ quan trọng để debug CI/CD.

## 6. Chỉ test "Golden Paths"
*   E2E rất chậm và tốn tài nguyên. Đừng test mọi edge case ở đây. Hãy để Unit/Integration test lo việc đó. Tập trung vào: Đăng ký, Đăng nhập, Thanh toán, luồng chính.
