# 🔐 Password Complexity Checker

This is a Python program that evaluates the **strength of passwords** and provides detailed feedback and suggestions for improvement.

---

## 📜 How It Works
- Analyzes the entered password against multiple criteria:
  - Length (minimum 8, strong if 12+)
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
  - Avoids common/weak passwords
  - Detects sequential patterns (e.g., `123`, `abc`)
  - Detects repeated characters (e.g., `aaa`, `111`)
- Provides a **strength rating**: Very Weak, Weak, Medium, Strong, Very Strong.
- Displays **feedback and suggestions** to improve your password.

---

## 🚀 Usage

1. Clone or download the script.
2. Run the Python file:

   ```bash
   python password_checker.py
   ```

3. Choose from the menu:
   - **Option 1:** Check password (visible while typing)
   - **Option 2:** Check password (hidden with `*` masking)
   - **Option 3:** View strength examples
   - **Option 4:** Exit

---

## 📝 Example Run

```
🔐 PASSWORD COMPLEXITY CHECKER
This tool will assess your password strength without storing it.

Options:
1. Check your password (visible)
2. Check your password (hidden)
3. View strength examples
4. Exit

Enter your choice (1-4): 1
Enter your password (visible): Password123!

============================================================
PASSWORD STRENGTH ANALYSIS
============================================================
Password: Password123!
Strength: 🟢 Strong (5/6 points)

DETAILED FEEDBACK:
  ✓ Minimum length met (8+ characters)
  ✓ Contains lowercase letters
  ✓ Contains uppercase letters (A-Z)
  ✓ Contains numbers (0-9)
  ✓ Contains special characters (!@#$% etc.)

SUGGESTIONS:
  • Increase length to 12+ characters for better security
  • Add more special characters
============================================================
```

---

## ⚙️ Requirements
- Python 3.x (no external libraries required)

---

## 📂 File Structure
```
password_checker.py   # Main program
README.md             # Documentation
```

---

## ✨ Features
- Evaluates password strength in real time
- Provides feedback and suggestions
- Detects weak patterns (common, sequential, repeated)
- Supports hidden password input (masked with `*`)
- Includes a loading animation for better UX
