# Quy tắc đặt tên (Naming Conventions)

Đặt tên là một trong những việc quan trọng nhất của Clean Code. Tên đúng giúp mã nguồn tự giải thích (Self-documenting).

## 1. Nguyên tắc chung
- **Chỉ dùng Tiếng Anh**: Tất cả biến, hàm, class và comment phải dùng tiếng Anh chuẩn.
- **Tính mô tả (Descriptive)**: Tên phải thể hiện được ý định.
  - *Bad*: `int d;`
  - *Good*: `int daysUntilExpiration;`
- **Tránh tên thừa (No Redundant Context)**: Nếu ở trong class `User`, đừng đặt biến là `userName`, chỉ cần `name` là đủ.
- **Không dùng Magic Numbers/Strings**: Luôn thay thế các giá trị hardcoded bằng hằng số (Constants) hoặc Enums.

## 2. Quy tắc Casing (Chuẩn .NET/General)
- **Classes / Interfaces**: `PascalCase` (VD: `UserController`, `IPaymentGateway`).
- **Methods / Functions**: `PascalCase` (C#) hoặc `camelCase` (JS) - theo chuẩn framework.
- **Variables / Properties**: `camelCase` (VD: `firstName`, `orderCount`).
- **Constants**: `UPPER_SNAKE_CASE` (VD: `MAX_RETRY_ATTEMPTS`).
- **Private Fields**: `_camelCase` (VD: `_userRepository`).

## 3. Quy ước theo loại dữ liệu
- **Booleans (Đúng/Sai)**: Sử dụng các tiền tố như `is`, `has`, `should`, `can`.
  - *VD*: `isActive`, `hasPermission`, `shouldRender`.
- **Collections (Danh sách)**: Luôn sử dụng danh từ **số nhiều**.
  - *VD*: `users`, `products`, `selectedItems`.
- **Hàm (Functions)**: Sử dụng cặp **Động từ - Danh từ**.
  - *VD*: `GetUser()`, `CalculateTax()`, `ValidateToken()`.

---

## 4. Cách báo cáo ISSUE (Mapping to Template)

| Vấn đề | Cấp độ | Vị trí | Giải thích |
| :--- | :--- | :--- | :--- |
| **Magic Number** | `?` | `File.cs` | Sử dụng số cụ thể (VD: `status == 1`) không có ý nghĩa. |
| **Tên biến vô nghĩa** | `?` | `File.cs` | Dùng các biến như `a`, `b`, `temp` gây khó hiểu. |
| **Sai Casing** | `*` | `File.cs` | Không tuân thủ chuẩn `PascalCase` cho class hoặc `camelCase` cho biến. |
| **Tiếng Việt trong code** | `!` | `File.cs` | Dùng tiếng Việt cho tên biến/hàm làm giảm tính chuyên nghiệp và khó bảo trì. |

---

## 5. Mẫu Refactor chuyên nghiệp

#### 🔴 Code Hiện Tại
```csharp
// ! Magic string và tên biến viết tắt
if (u.stt == "act") {
    var d = 10;
}
```

#### 🟢 Code Đề Xuất
```csharp
// # Sử dụng Enum và tên mô tả
if (user.Status == UserStatus.Active) {
    const int GRACE_PERIOD_DAYS = 10;
    var expirationDate = DateTime.Now.AddDays(GRACE_PERIOD_DAYS);
}
```
