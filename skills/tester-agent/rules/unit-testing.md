# Unit Testing Rules

Unit Test là nền tảng của Test Pyramid. Chúng phải cực kỳ nhanh, cô lập và tập trung vào logic nghiệp vụ (business logic).

## 1. Tính độc lập & Cô lập (Isolation)
*   **KHÔNG** truy cập Database thật. Dùng Repository Pattern và Mock chúng.
*   **KHÔNG** gọi API bên ngoài. Dùng `Http::fake()` hoặc Mock Service Client.
*   **KHÔNG** dùng File System thật. Dùng `Storage::fake()`.
*   **Ý nghĩa**: Nếu code logic đúng nhưng DB chết, Unit Test vẫn phải PASS.

## 2. Cấu trúc AAA (Arrange - Act - Assert)
*   Mỗi test case phải chia rõ 3 khối này.
*   **Arrange**: Khởi tạo Object, Fake dữ liệu, Mock dependencies.
*   **Act**: Gọi duy nhất 1 function cần test.
*   **Assert**: Kiểm tra kết quả trả về hoặc thuộc tính thay đổi.

## 3. Quy tắc đặt tên (Naming)
*   Ưu tiên phong cách mô tả hành vi: `it_should_[expected]_[condition]`.
*   Ví dụ: `it_should_calculate_discount_when_coupon_is_valid`.
*   Tránh tên chung chung như `test_calculation`.

## 4. Test Edge Cases (Biên)
*   Đừng chỉ test "Happy Path". Hãy test:
    *   Input là `null`, `[]`, `''`.
    *   Số âm, số 0 cho các hàm tính toán.
    *   Dữ liệu cực lớn (Max Interger).
    *   Ký tự lạ (Emoji, Unicode).

## 5. Tốc độ thực thi
*   Mục tiêu: < 20ms cho mỗi Unit Test.
*   Nếu test chạy lâu (> 100ms), xem lại xem bạn có đang vô tình nạp quá nhiều dependencies hoặc chạm vào ổ đĩa không.

## 6. Assertion Chặt chẽ
*   Tránh `assertTrue(true)` vô nghĩa.
*   Assert chính xác type và giá trị: `assertEquals(10.5, $result)` tốt hơn `assertNotNull($result)`.
