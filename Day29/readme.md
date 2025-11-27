# Password Manager

## 📝 Program Overview

A desktop password manager application built with Python's Tkinter library. This program allows users to:
- Generate random secure passwords with one click
- Store website credentials (website, username/email, password)
- Save all passwords to a text file (`data.txt`)
- Automatically copy generated passwords to clipboard

**Current Features:**
- GUI interface with logo
- Random password generator (includes letters, numbers, and symbols)
- Input fields for website, email/username, and password
- "Generate Password" button that creates secure passwords
- "Add" button to save credentials to file
- Popup confirmation dialog when password is saved
- All magic numbers extracted to constants at the top of the file

---

## 🚀 Known Limitations & Future Improvements

### 🔴 Security & Reliability Issues

1. **Plain-text password storage** - Passwords are currently saved unencrypted in `data.txt`. This is a security risk. Future versions should implement encryption using libraries like `cryptography.fernet`.

2. **No error handling** - File operations lack try-except blocks. The program may crash if `data.txt` cannot be written or if `logo.png` is missing.

### 🟡 Code Quality Improvements

3. **Fragile data format** - Uses pipe-separated values (`|`). If a user enters `|` in their website name, the data format breaks. Should migrate to JSON or CSV:
   ```python
   import json
   data = {"website": website, "username": username, "password": password}
   ```

4. **Global variables** - All widgets and state are global. Should refactor to a `PasswordManager` class for better organization.

5. **Hardcoded file paths** - `data.txt` and `logo.png` use relative paths. Should use `os.path.join()` or `pathlib` for cross-platform compatibility.

### 🟢 Feature Enhancements

6. **Search functionality** - No way to retrieve saved passwords. Should add a search button to find credentials by website name.

7. **Edit/Delete operations** - Users cannot modify or remove saved passwords.

8. **Password strength indicator** - No feedback on whether generated password is weak/medium/strong.

9. **Configurable default email** - Email address is hardcoded as a constant. Should be user-configurable via settings.

10. **Clipboard security** - Generated passwords remain in clipboard indefinitely. Should auto-clear after 30 seconds.

---
