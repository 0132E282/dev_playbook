# 💎 Clean Code & Best Practices

## 1. Core Philosophy
- **Code for Humans**: Write code to be read by others, not just the machine.
- **KISS (Keep It Simple)**: Avoid over-engineering. Clear is better than clever.
- **YAGNI**: "You Ain't Gonna Need It". Don't implement features for a hypothetical future.

## 2. Naming Conventions (**Critical**)
- **No Abbreviations**: **Do not abbreviate** unless the word is extremely long or the abbreviation is a standard industry term (e.g., `id`, `html`).
    - ❌ Bad: `usr`, `cust`, `addr`, `tst`
    - ✅ Good: `user`, `customer`, `address`, `test`
    - *rationale*: Abbreviations cause ambiguity and misunderstanding. Explicit is always better.
- **Variables/Functions**: Use `camelCase`.
    - Variables: Nouns (e.g., `maxRetryCount`, `isValid`).
    - Functions: Verb-noun (e.g., `getUserById`, `validateUser`).
- **Classes**: Use `PascalCase` (e.g., `UserService`, `PaymentController`).
- **Constants**: Use `UPPER_SNAKE_CASE` (e.g., `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`).

## 3. Functions & Methods
- **SRP (Single Responsibility)**: A function should do **one thing** only.
    - ❌ Bad: `createUser` that validates, saves, AND emails.
    - ✅ Good: `createUser` calls `validateUser`, `saveUser`, `sendWelcomeEmail`.
- **Length**: keep functions short. If it's too long, split it.
- **Early Returns**: Avoid nested `if/else` hell. Return as soon as possible.
    ```javascript
    // ✅ Good
    if (!isValid) return;
    if (!hasPermission) return;
    doSomething();
    ```

## 4. Code Quality & Logic
- **No Magic Numbers/Strings**: Use constants.
    - ❌ `if (status === 3)`
    - ✅ `const ORDER_PAID = 3; if (status === ORDER_PAID)`
- **DRY (Don't Repeat Yourself)**: If you copy-paste code, refactor it into a shared function.
- **Explicit Logic**:
    - ❌ `return a && b && c` (Hard to debug)
    - ✅ `const canView = hasPermission && isActive; return canView;`

## 5. Error Handling
- **Always Handle Errors**: Catch exceptions where appropriate. Don't let the app crash silently.
- **No Silent Failures**: **NEVER** use empty catch blocks (`try { ... } catch (e) {}`).
    - *Why*: This wraps the error in silence, making debugging a nightmare.
- **Meaningful Logs**: Log context, not just the error.
    - ❌ `console.error(err)`
    - ✅ `logger.error('Failed to process payment', { orderId: 123, error: err.message })`
- **Typed Exceptions**: Throw specific exceptions (e.g., `UserNotFoundException`) instead of generic errors.

## 6. Comments
- **Explain "Why", not "What"**: Code tells what happens; comments explain the business context.
    - ❌ `// Loop users` (Redundant)
    - ✅ `// Batch process users to reduce DB connections`
- **Self-Documenting Code**: If the code is clear, you don't need comments.
    - *Rule*: Rename variables/functions to be clearer before adding an explanatory comment.
- **Avoid Commented-Out Code**: Delete it. Git has history if you need it back.

## 7. Format & Style
- **Indentation**: Choose **2 spaces** or **4 spaces** and stick to it strictly. Never mix tabs and spaces.
- **Braces**: Use K&R style (opening brace on the same line).
    ```javascript
    // ✅ Good
    if (isValid) {
        ...
    }
    ```
- **Line Length**: Soft limit at 80-100 characters. Horizontal scrolling is a sin.
- **Vertical Spacing**:
    - Add a blank line between methods/functions.
    - Add a blank line between logical steps inside a function to create "paragraphs".
- **Ordering**:
    1. Imports / Dependencies
    2. Constants / Types
    3. Properties
    4. Constructor
    5. Public Methods
    6. Private Methods
    - **Trailing Commas**: Recommended in multi-line arrays/objects (makes git diffs cleaner).

## 8. Review Mindset
- **The "3-Month" Rule**: Will you understand this code in 3 months without context?
- **Simplicity Test**: If you have to explain code with a 5-minute drawing, it's too complex. Refactor it.
- **Automate**: Use tools like **Prettier**, **ESLint**, or **PHP-CS-Fixer** to handle formatting automatically. Don't argue about spaces in PRs.
