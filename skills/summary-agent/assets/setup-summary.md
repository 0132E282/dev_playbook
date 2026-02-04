# 🛠️ Hướng dẫn Cài đặt & Yêu cầu Hệ thống

## 📋 Yêu cầu tiên quyết (Prerequisites)
- **SDK/Runtime**: {{Version ví dụ: .NET 8.0, Node.js v20}}
- **Database**: {{Version ví dụ: PostgreSQL 15, SQL Server 2022}}
- **Công cụ**: {{Ví dụ: Docker Desktop, Make, Git}}

## ⚙️ Cấu hình (Configuration)
Các bước thiết lập môi trường:
1. **File biến môi trường**: Sao chép `{{FileExample}}` thành `{{FileTarget}}`.
2. **Key quan trọng**: `{{List các key cần chú ý}}`.

## 🚀 Các bước cài đặt
```bash
# Cài đặt dependency
{{InstallCommand}}

# Thiết lập database (nếu có)
{{DBCommand}}
```

## 🏃 Lệnh chạy dự án
```bash
# Chạy ở chế độ Development
{{DevCommand}}

# Chạy ở chế độ Production
{{ProdCommand}}
```

## ✅ Kiểm tra trạng thái
- **API URL**: `{{URL ví dụ: http://localhost:5000/swagger}}`
- **Health Check**: `{{URL Check}}`
- **Dấu hiệu chạy đúng**: {{Mô tả kết quả mong đợi}}
