# Nguyên Tắc Clean Code chuyên sâu

Tài liệu này định nghĩa các tiêu chuẩn vàng về mã nguồn sạch, giúp bạn đưa ra các nhận xét chính xác trong `review-summary-template.md`.

## 1. Nguyên tắc SOLID

### S - Single Responsibility (Đơn nhiệm)
- Một class/hàm chỉ nên có **một lý do duy nhất** để thay đổi.
- **Kiểm tra**: Class có đang vừa xử lý logic, vừa gọi DB, vừa gửi email không? Nếu có, hãy tách ra.

### O - Open/Closed (Đóng/Mở)
- Mở rộng tính năng bằng cách thêm mới, không sửa đổi code cũ đã chạy ổn định.
- **Kiểm tra**: Khi thêm một loại thanh toán mới, bạn có phải sửa `switch-case` cũ không? Nếu có, hãy dùng **Strategy Pattern** hoặc **Polymorphism**.

### L - Liskov Substitution (Thay thế Liskov)
- Class con phải có khả năng thay thế hoàn toàn class cha mà không làm thay đổi tính đúng đắn của chương trình.
- **Kiểm tra**: Class con có throw `NotImplementedException` cho một hàm của cha không? Nếu có, cấu trúc thừa kế đang sai.

### I - Interface Segregation (Phân tách Interface)
- Thà nhiều interface nhỏ, chuyên biệt còn hơn một interface lớn mà chứa các hàm không liên quan.
- **Kiểm tra**: Class có phải implement các hàm rỗng chỉ để thỏa mãn interface không? Nếu có, hãy tách interface.

### D - Dependency Inversion (Đảo ngược phụ thuộc)
- Phụ thuộc vào Abstraction (Interface), không phụ thuộc vào Implementation (Class cụ thể).
- **Kiểm tra**: Bạn có đang dùng `new Service()` trực tiếp trong Controller không? Hãy sử dụng **Dependency Injection**.

---

## 2. Các nguyên tắc tối thượng khác

### KISS (Keep It Simple, Stupid) - Giữ mọi thứ đơn giản
- Đừng làm phức tạp hóa vấn đề. Giải pháp đơn giản nhất thường là giải pháp tốt nhất.
- **Check**: Code có đang bị over-engineering (thiết kế quá mức cần thiết) không?

### DRY (Don't Repeat Yourself) - Không lặp lại chính mình
- Tuyệt đối không copy-paste logic. Nếu lặp > 2 lần, hãy đóng gói thành hàm hoặc service dùng chung.

### YAGNI (You Ain't Gonna Need It) - Chưa cần thì đừng làm
- Chỉ lập trình những gì cần thiết cho yêu cầu hiện tại. Đừng thêm code cho "tương lai xa vời".

### Composition over Inheritance - Ưu tiên gộp thành phần
- Ưu tiên sử dụng Composition để lắp ghép tính năng thay vì thừa kế nhiều cấp (> 3 cấp).

---

## 3. Cách báo cáo ISSUE (Mapping to Template)

| Vấn đề | Cấp độ | Vị trí | Giải thích |
| :--- | :--- | :--- | :--- |
| **Vi phạm SRP** | `!` | `File.cs` | Class làm quá nhiều việc, khó Unit Test. |
| **Over-engineering** | `?` | `File.cs` | Giải pháp quá phức tạp so với yêu cầu đơn giản. |
| **Lặp code (WET)** | `?` | `File.cs` | Logic tương tự xuất hiện ở nhiều nơi. |
| **Hard-dependency** | `!` | `File.cs` | Khởi tạo object trực tiếp thay vì Inject Interface. |

---

## 4. Mẫu Refactor chuyên nghiệp

#### 🔴 Code Hiện Tại
```csharp
public class OrderService {
    public void Process(Order order) {
        // Xử lý đơn hàng
        // Gửi email (Vi phạm SRP)
        // Lưu log vào file (Vi phạm SRP)
    }
}
```

#### 🟢 Code Đề Xuất
```csharp
public class OrderProcessor {
    public OrderProcessor(IEmailService mailer, ILogger logger) { ... }

    public void Process(Order order) {
        // # SRP: Chế xử lý nghiệp vụ chính
        // # DIP: Gọi qua Interface
        _mailer.Send(order);
    }
}
```
