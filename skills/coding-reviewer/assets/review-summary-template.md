# Mẫu Tổng Hợp Review Code

Sử dụng mẫu này khi tổng hợp kết quả review code.

## 🏁 Tổng Quan

**Trạng thái**: {{APPROVE (Chấp thuận) | REQUEST_CHANGES (Yêu cầu sửa) | COMMENT (Góp ý)}}

### 🛡️ Bảo Mật (Security)
- [ ] Kiểm tra Input Validation (Validate đầu vào)
- [ ] Không lộ Secrets/Hardcoded Keys
- [ ] Kiểm tra phân quyền (Authorization) có đầy đủ

### ⚡ Hiệu Năng (Performance)
- [ ] Không lỗi N+1 Queries
- [ ] Tối ưu Loops/Maps
- [ ] Sử dụng Database Indexing hợp lý

### 🧹 Clean Code
- [ ] Tuân thủ quy tắc đặt tên (Naming Conventions)
- [ ] Nguyên tắc Single Responsibility (SRP)
- [ ] DRY (Không lặp code)

---

## 📝 Chi Tiết Review

> Copy block dưới đây cho mỗi vấn đề tìm thấy.

### 1. [Tên vấn đề tóm tắt]
- **Mức độ**: `[Tag]` [Mức độ] (VD: `!` NGHIÊM TRỌNG, `?` CẢNH BÁO, `*` GỢI Ý, `#` TỐT)
- **File**: `[Đường dẫn file]` (Dòng [x])
- **BigO**: [Độ phức tạp] - [Đánh giá hiệu suất]
- **Vấn Đề & Phân Tích**:
  [Mô tả chi tiết ngữ cảnh lỗi]
  - 🧹 **Clean Code**: [Chỉ rõ điểm vi phạm - VD: Tên biến sai quy tắc, hàm quá dài, vi phạm SRP...]
  - ⚡ **Hiệu Năng**: [Chỉ rõ điểm gây chậm - VD: Query dư thừa, thuật toán độ phức tạp cao...]
  - 🛡️ **Bảo Mật**: [Chỉ rõ nguy cơ - VD: Thiếu validate, XSS, SQL Injection...]
- **Đề xuất**: [Mô tả giải pháp cụ thể, logic xử lý. Luôn đề xuất hướng Refactor nếu mã chưa Clean]

---

## 🔍 So Sánh Chi Tiết (Code Hiện Tại vs Đề Xuất)

> Copy section này cho mỗi file cần review chi tiết.

### 📂 File: `[Đường dẫn file]`

#### 🔴 Code Hiện Tại (Dòng [x]-[y])
```[language]
// Code gốc có vấn đề
```

#### 🟢 Code Đề Xuất
```[language]
// Code đã được tối ưu
```

**Giải thích**:
- [Giải thích lý do thay đổi]
- [Lợi ích của việc thay đổi]

---

## 💡 Gợi Ý Hàng Đầu
1. ...
2. ...
