# Security Audit Checklist Template

Use this for dedicated security reviews.

## 🔒 Security Audit Report

**Target**: `[Feature/Module Name]`
**Date**: `YYYY-MM-DD`

### 1. Injection Flaws
- [ ] **SQL Injection**: No raw queries with user input.
- [ ] **XSS**: No unescaped output in views (`{!! !!}` or `dangerouslySetInnerHTML`).
- [ ] **Command Injection**: No `exec()` or `system()` with user input.

### 2. Authentication & Authorization
- [ ] **IDOR**: Users cannot access resources of others by ID change.
- [ ] **CSRF**: Forms have tokens.
- [ ] **RBAC**: Middleware checks roles/permissions.

### 3. Data Protection
- [ ] **Secrets**: No API Keys/Credentials in code.
- [ ] **PII**: No sensitive user data logged.
- [ ] **HTTPS**: Links/Assets use secure protocol.

### 4. Input Validation
- [ ] **Type Checking**: Inputs are type-casted.
- [ ] **Length Limits**: Strings have max lengths.
- [ ] **Sanitization**: Inputs are cleaned.

## 🚨 Critical Findings

1. ...
2. ...
