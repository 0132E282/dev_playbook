# Hướng Dẫn Review & Viết Test

Tài liệu này định nghĩa các tiêu chuẩn khi review và viết test, nhằm đảm bảo chất lượng code có thể được báo cáo chính xác theo mẫu `review-summary-template.md`.

## 1. Tiêu Chí Review Test (Review Criteria)

Khi review các file test (Unit/Integration Tests), hãy áp dụng 3 trụ cột chính từ template:

### 🧹 Clean Code trong Testing
- **Tên Test (Naming)**: Phải mô tả rõ: **Ngữ cảnh + Hành động + Kết quả mong đợi**.
  - *Ví dụ tốt*: `CalculateTotal_WithValidItems_ReturnsCorrectSum`
  - *Ví dụ xấu*: `Test1`, `CheckPrice`
- **Cấu trúc AAA**: Luôn tuân thủ **Arrange (Chuẩn bị), Act (Thực thi), Assert (Kiểm chứng)**.
- **Tính đơn nhiệm (SRP)**: Mỗi hàm test chỉ nên kiểm chứng **một kết quả cụ thể**. Tránh việc nhồi nhét quá nhiều Assert không liên quan vào một test case.

### ⚡ Hiệu Năng (Performance trong Test)
- **BigO & Speed**: Test phải chạy nhanh. Nếu một Unit Test có độ phức tạp thuật toán quá cao hoặc loop quá nhiều data giả, hãy đánh dấu là `? CẢNH BÁO`.
- **Cô lập (Isolation)**: Unit Test **phải** sử dụng Mock/Substitute cho các phụ thuộc bên ngoài (DB, API). Nếu test gọi DB thật, đó là `! NGHIÊM TRỌNG` (vi phạm tính chất Unit Test).

### 🛡️ Bảo Mật (Security trong Test)
- **Data Nhạy Cảm**: Không bao giờ sử dụng credential thật, API key thật trong code test.
- **Kiểm thử phân quyền**: Luôn có các test case cho trường hợp `Unauthorized` hoặc `Forbidden` để đảm bảo logic bảo mật không bị bypass.

---

## 2. Cách Báo Cáo Issue Trong Test (Mapping to Template)

Khi phát hiện lỗi trong code test, hãy điền vào `review-summary-template.md` như sau:

| Vấn đề | Cấp độ | Vị trí | Cách báo cáo |
| :--- | :--- | :--- | :--- |
| **Logic sai** | `!` | `TestFile.cs` | Chỉ rõ kết quả Assert đang kỳ vọng sai so với nghiệp vụ. |
| **Thiếu Edge Case** | `?` | `TestFile.cs` | Yêu cầu bổ sung test cho case: Null, Empty, OutOfRange. |
| **N+1 trong Integration Test** | `?` | `IntegrationTest.cs` | Cảnh báo nếu một loop trong test gây ra quá nhiều query ngầm. |
| **Hardcoded ID/Data** | `*` | `TestFile.cs` | Gợi ý dùng AutoFixture hoặc Faker để tạo data ngẫu nhiên. |

---

## 3. Checklist Nhanh Khi Review Test

- [ ] **Arrange**: Data giả có sát với thực tế không?
- [ ] **Act**: Hàm được gọi có đúng là Unit cần test không (System Under Test - SUT)?
- [ ] **Assert**: Có kiểm tra cả trường hợp lỗi (Exception) không?
- [ ] **Cleanliness**: Code test có dễ đọc như code logic không? (Test code is first-class citizen).
- [ ] **Independence**: Các test case có chạy độc lập không? (Kết quả test A không được ảnh hưởng test B).

---

## 4. Mẫu So Sánh Đề Xuất (Trong Template)

#### 🔴 Code Hiện Tại
```csharp
[Fact]
public void TestEmail() {
    var service = new EmailService(); // ! NGHIÊM TRỌNG: Khai báo trực tiếp không qua Mock
    service.Send("test@gmail.com");
    Assert.True(true); // ? CẢNH BÁO: Assert vô nghĩa
}
```

#### 🟢 Code Đề Xuất
```csharp
[Fact]
public void SendEmail_WithValidRecipient_CallsMailProviderOnce() {
    // Arrange
    var mockProvider = new Mock<IMailProvider>();
    var sut = new EmailService(mockProvider.Object);

    // Act
    sut.Send("test@gmail.com");

    // Assert
    mockProvider.Verify(x => x.Send(It.IsAny<string>()), Times.Once);
}
```
