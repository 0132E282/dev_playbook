# Clean Testing Cheat Sheet

Tóm tắt 12 quy tắc "bất di bất dịch" cho mọi Test Engineer.

## 🔥 The 12 Golden Rules

1.  **Independent**: Test A không phụ thuộc Test B.
2.  **Atomicity**: 1 Test = 1 Hành vi.
3.  **Naming**: `it_should_do_X_when_Y`.
4.  **Behavior only**: Test Input -> Output. Không test private method.
5.  **AAA**: Arrange -> Act -> Assert.
6.  **Isolation**: Mock hết DB, API, File System trong Unit Test.
7.  **Speed**: Chậm là chết.
8.  **Pyramid**: Nhiều Unit, Ít E2E.
9.  **Edge Case**: Null, Empty, Max, Min, Error.
10. **Quality > Coverage**: Đừng chạy theo con số %.
11. **Regression**: Có bug -> Viết test -> Fix.
12. **Design Tool**: Test khó viết -> Code cần Refactor.

## 💡 Code Patterns (PHP/JS)

### AAA Pattern
```php
// Bad
$user = User::create(['name' => 'A']);
$this->assertTrue($user->exists);

// Good
public function test_user_creation() {
    // Arrange
    $data = ['name' => 'Alice', 'email' => 'alice@test.com'];

    // Act
    $user = $this->userService->create($data);

    // Assert
    $this->assertEquals('Alice', $user->name);
    $this->assertDatabaseHas('users', ['email' => 'alice@test.com']);
}
```

### Mocking (Laravel Example)
```php
// Cần test Service gọi API bên ngoài
// Arrange
Http::fake([
    'github.com/*' => Http::response(['id' => 1], 200)
]);

// Act
$result = $service->fetchGithubProfile('user');

// Assert
$this->assertEquals(1, $result['id']);
```

### Testing Exceptions
```php
// PHP (Pest)
expect(fn() => $calculator->divide(10, 0))->toThrow(DivisionByZeroError::class);

// JS (Jest/Vitest)
expect(() => calculator.divide(10, 0)).toThrow('Division by zero');
```

### Naming Conventions
| Type | Pattern | Example |
|------|---------|---------|
| **Unit** | `method_condition_result` | `calculate_total_with_empty_cart_returns_zero` |
| **Behavior** | `it_should_..._when_...` | `it_should_lock_account_when_3_failed_attempts` |
| **Bug** | `issue_[id]_[description]` | `issue_102_fix_login_race_condition` |
