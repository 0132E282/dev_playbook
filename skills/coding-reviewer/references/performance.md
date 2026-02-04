# Tối ưu Hiệu năng (Performance Rules)

Tài liệu này hướng dẫn cách phát hiện và khắc phục các vấn đề về tốc độ, bộ nhớ và tài nguyên hệ thống.

## 1. Tối ưu Database
- **Lỗi N+1 Query**: Phát hiện các vòng lặp thực hiện query liên tục. Luôn sử dụng Eager Loading (`Include` trong EF Core, `with` trong Laravel).
- **Indexing**: Đảm bảo các cột trong mệnh đề `WHERE`, `ORDER BY`, và `JOIN` được đánh Index chính xác.
- **Specific Selection**: Tránh dùng `SELECT *`. Chỉ lấy những cột cần thiết cho nghiệp vụ (Sử dụng `Select()` hoặc DTO).
- **Bulk Operations**: Sử dụng insert/update hàng loạt (bulk) thay vì lặp từng dòng để lưu.

## 2. Hiệu quả mã nguồn (Code Efficiency)
- **Loops & I/O**: Tuyệt đối không gọi DB, API hoặc thao tác File bên trong vòng lặp `for/foreach`. Hãy lấy dữ liệu ra ngoài trước (Batch fetch).
- **Bộ nhớ (Memory)**: Khi xử lý dữ liệu lớn, sử dụng `Streaming`, `Chunking` hoặc `Generators` để tránh tràn bộ nhớ (OutOfMemory).
- **Độ phức tạp (Big O)**: Cảnh giác với các vòng lặp lồng nhau (Nested loops) dẫn đến độ phức tạp $O(n^2)$ hoặc $O(n^3)$ trên các tập dữ liệu lớn.

## 3. Quản lý Cache
- **Cache High-Read/Low-Write**: Sử dụng Redis/In-memory cache cho dữ liệu ít thay đổi nhưng được đọc thường xuyên (VD: Config, Categories).
- **Cache Invalidation**: Phải có chiến lược xóa/cập nhật cache (TTL, Observer) để tránh hiển thị dữ liệu cũ (Stale data).

---

## 4. Cách báo cáo ISSUE (Mapping to Template)

| Vấn đề | Cấp độ | Vị trí | Giải thích | BigO |
| :--- | :--- | :--- | :--- | :--- |
| **N+1 Query** | `!` | `Repo/Service` | Thực hiện hàng chục query trong 1 request. | $O(N)$ query |
| **Logic trong Loop** | `?` | `Service.cs` | Gọi Service/DB bên trong vòng lặp. | $O(N)$ I/O |
| **Thiếu Index** | `?` | `Database` | Query trên bảng lớn mà không qua Index. | $O(N)$ scan |
| **SELECT *** | `*` | `Repo.cs` | Lấy dữ liệu thừa không cần thiết (VD: lấy cả Content cho list). | High Payload |

---

## 5. Mẫu Refactor chuyên nghiệp

#### 🔴 Code Hiện Tại (Dòng 50-60)
```csharp
// ! NGHIÊM TRỌNG: N+1 Query và Query trong vòng lặp
var orders = _context.Orders.ToList();
foreach(var order in orders) {
    var user = _context.Users.Find(order.UserId); // Query mỗi lần lặp
}
```

#### 🟢 Code Đề Xuất
```csharp
// # Eager Loading: Chỉ dùng 1 Query duy nhất
var orders = await _context.Orders
    .Include(o => o.User) // # Load User ngay lập tức
    .Select(o => new { o.Id, UserName = o.User.Name }) // # Chỉ lấy field cần thiết
    .ToListAsync();
```

**Giải thích**: Chuyển từ $N$ query xuống còn $1$ query duy nhất bằng cách sử dụng `Include`. Giảm tải cực lớn cho Database Server.
