# QA / Testing Checklist

Sử dụng checklist này khi review Pull Request hoặc trước khi merge code vào main branch.

## 1. Unit Test Health
- [ ] **Naming Standard**: Tên test có tuân thủ format `it_should_[behavior]_when_[condition]` không?
- [ ] **Independence**: Test có chạy độc lập không? (Không phụ thuộc DB state cũ, không gọi API thật).
- [ ] **AAA Pattern**: Code có phân chia rõ ràng 3 phần Arrange - Act - Assert không?
- [ ] **Assertions**:
    - [ ] Không assert chung chung (`assertTrue($result)`).
    - [ ] Message lỗi có rõ ràng không?
- [ ] **Mocking**: Tất cả dependencies (Repo, Service, API) đã được mock chưa?

## 2. Coverage & Scenarios
- [ ] **Happy Path**: Trường hợp thành công thông thường.
- [ ] **Edge Cases**:
    - [ ] Null / Undefined / Empty inputs.
    - [ ] Boundary values (0, -1, max_int).
    - [ ] Special characters / SQL Injection payloads.
- [ ] **Error Handling**: Test case cho việc throw Exception hoặc return Error Code.

## 3. Integration / E2E (Nếu có)
- [ ] **Clean State**: Database có được clean sau khi chạy test không?
- [ ] **Selectors**: Sử dụng `getByRole`, `getByText` thay vì XPath dễ gãy.
- [ ] **Wait**: Không sử dụng hard wait (`sleep(5)`).
- [ ] **Performance**: Query SQL trong test có được tối ưu không (tránh N+1 khi seed data)?

## 4. Maintenance
- [ ] Code test có bị Duplicate không? (Nên dùng `setUp`, `beforeEach` hoặc Factory).
- [ ] Test chạy có nhanh không? (Unit test < 50ms).
