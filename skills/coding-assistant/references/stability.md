# 🛡️ Operational Stability Rules

To ensure reliable agent operation, strict adherence to these rules is mandatory.

## 1. Safety First
- **No Blind Edits**: Never modify a file without reading it first (`view_file`).
- **Atomic Commits**: Break large refactors into small, verifiable steps.
- **Dependency Checks**: Verify imports/packages exist before using them.

## 2. Regression Prevention
- **Backwards Compatibility**: Ensure new code supports existing data structures.
- **Fallbacks**: Always implement fallback mechanisms for critical features.
- **Tests**: If possible, verify changes with existing tests before committing.

## 3. Data Integrity
- **No Hard Deletes**: Prefer soft deletes or commenting out code over permanent removal until fully verified.
- **Sanitization**: Never hardcode credentials, secrets, or PII.

## 4. User Communication
- **Clarify Ambiguity**: If a request is vague, ask for clarification before guessing.
- **Transparency**: clearly state *what* you are changing and *why*.
