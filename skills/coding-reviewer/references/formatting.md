# Quy tắc Định dạng Code (Formatting Rules)

Tài liệu này định nghĩa các tiêu chuẩn về hình thức của mã nguồn, tập trung vào tính nhất quán và dễ đọc, dựa trên tiêu chuẩn của **Prettier** và các Best Practices hiện đại.

## 1. Tiêu chuẩn Prettier (Frontend & General)
Đối với các file JavaScript, TypeScript, JSON, HTML, CSS (đặc biệt trong thư mục `ClientApp`):

- **Tab Width**: 2 spaces (Sử dụng 2 khoảng trắng cho mỗi cấp độ thụt lề).
- **Semi-colons**: `true` (Luôn có dấu chấm phẩy ở cuối câu lệnh).
- **Quotes**: `single` (Ưu tiên dùng dấu nháy đơn `'` thay vì nháy kép `"`).
- **Trailing Comma**: `all` (Luôn có dấu phẩy ở phần tử cuối cùng trong object/array nhiều dòng để dễ diff/merge).
- **Print Width**: 80 - 100 characters (Tự động xuống dòng khi câu lệnh quá dài).
- **Bracket Spacing**: `true` (Có khoảng trắng giữa ngoặc nhọn và nội dung. VD: `{ user }`).
- **Arrow Function Parentheses**: `always` (Luôn có ngoặc cho tham số arrow function. VD: `(x) => x`).

## 2. Tiêu chuẩn C# / .NET (Backend)
Đối với mã nguồn C#, mặc dù Prettier ít dùng hơn nhưng cần tuân thủ cấu trúc gọn gàng:

- **Indentation**: 4 spaces (Thụt lề 4 khoảng trắng).
- **Braces**: K&R hoặc Allman style (Tùy cấu hình project, nhưng phải nhất quán).
- **Line Breaks**: Giữa các phương thức phải có 1 dòng trống.
- **Imports (Using)**: Sắp xếp theo thứ tự bảng chữ cái và loại bỏ các using không sử dụng.

## 3. Quy tắc "Mắt thường" (Visual Rules)
- **Vertical Whitespace**: Sử dụng dòng trống để phân tách các khối logic trong cùng một hàm.
- **Max File Length**: Một file không nên vượt quá 400 dòng. Nếu quá dài, hãy cân nhắc tách file.
- **Nested Levels**: Giới hạn tối đa 3 cấp độ lồng nhau (if inside for inside if). Nếu sâu hơn, hãy tách hàm.

---

## 4. Cách báo cáo ISSUE (Mapping to Template)

| Vấn đề | Cấp độ | Vị trí | Giải thích |
| :--- | :--- | :--- | :--- |
| **Sai thụt lề** | `*` | `Code` | Thụt lề không nhất quán (lúc 2 lúc 4). |
| **Thiếu dấu chấm phẩy** | `*` | `JS/TS` | Vi phạm quy tắc Prettier đã đề ra. |
| **Logic lồng quá sâu** | `?` | `Function` | Code lồng nhau > 3 cấp, cực kỳ khó đọc. |
| **File quá dài** | `?` | `File` | File chứa hàng nghìn dòng code, vi phạm tính bảo trì. |

---

## 5. Mẫu Refactor chuyên nghiệp

#### 🔴 Code Hiện Tại (Lộn xộn, không format)
```javascript
function login(u,p){
if(u){if(p){
const auth={user:u,pass:p}
return doLogin(auth)}}
}
```

#### 🟢 Code Đề Xuất (Theo Prettier)
```javascript
// # Định dạng rõ ràng, thụt lề 2 spaces
const login = (user, password) => {
  if (!user || !password) return null;

  const auth = { user, password }; // # Bracket spacing & Trailing comma
  return doLogin(auth);
};
```
