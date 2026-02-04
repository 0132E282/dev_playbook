# Integration Testing Rules

Integration Test kiểm tra sự tương tác giữa code của bạn và các hệ thống bên ngoài (DB, Mail, Queue) hoặc giữa các module với nhau.

## 1. Quản lý trạng thái DB
*   Sử dụng **Transaction Rollback** hoặc **RefreshDatabase** trait để đảm bảo mỗi test case có một DB "sạch".
*   KHÔNG viết test phụ thuộc vào ID tự tăng (e.g. `assertEquals(1, $user->id)` là sai vì ID có thể khác nhau tùy môi trường).

## 2. Sử dụng Factory & Seeders
*   Dùng **Model Factories** để tạo dữ liệu giả lập có cấu trúc đúng.
*   Chỉ tạo những gì tối thiểu cần thiết cho test để tránh làm chậm test suite.

## 3. Test API Contract
*   Assert cấu trúc JSON trả về (`assertJsonStructure`).
*   Check HTTP Status Code (200, 201, 422, 401, 403, 500).
*   Kiểm tra logic phân quyền (Authorize): User A không được sửa dữ liệu của User B.

## 4. Kiểm tra Side-Effects
*   Integration test nên kiểm tra xem record đã được lưu vào DB chưa (`assertDatabaseHas`).
*   Kiểm tra Job có được đẩy vào Queue không (`Queue::assertPushed`).
*   Kiểm tra Event có được bắn ra không (`Event::assertDispatched`).

## 5. Tối ưu hóa hiệu năng
*   Tránh tạo quá nhiều dữ liệu mẫu nếu không cần thiết.
*   Sử dụng In-memory Database (SQLite) nếu tốc độ là vấn đề, nhưng hãy cẩn thận vì SQLite có thể không hỗ trợ đủ cú pháp như MySQL/Postgres.
