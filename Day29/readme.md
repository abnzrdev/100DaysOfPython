# Password Manager

## 📝 Program Overview

A desktop password manager application built with Python's Tkinter library. This program allows users to:
- Generate random secure passwords with one click
- Store website credentials (website, username/email, password)
- Save all passwords to a JSON file (`data.json`)
- Search for saved passwords by website name
- Automatically copy generated/retrieved passwords to clipboard

**Current Features:**
- GUI interface with logo
- Random password generator (includes letters, numbers, and symbols)
- Input fields for website, email/username, and password
- "Generate Password" button that creates secure passwords
- "Search Password" button to retrieve saved credentials
- "Add" button to save credentials to file
- Popup confirmation dialog when password is saved
- All magic numbers extracted to constants at the top of the file
- **JSON storage format** for reliable data persistence
- **Comprehensive error handling** for file operations, JSON parsing, and clipboard access
- **Graceful fallbacks** when logo fails to load or data file is missing/corrupted

---

## 🚀 Known Limitations & Future Improvements

### 🔴 Security & Reliability Issues

1. **Plain-text password storage** - Passwords are currently saved unencrypted in `data.json`. This is a security risk. Future versions should implement encryption using libraries like `cryptography.fernet`.

### 🟢 Feature Enhancements

5. **Edit/Delete operations** - Users cannot modify or remove saved passwords. Should add edit and delete buttons in search results.

6. **Password strength indicator** - No visual feedback on whether generated password is weak/medium/strong. Could add a strength meter.

7. **Configurable default email** - Email address is hardcoded as a constant. Should be user-configurable via settings dialog.

8. **Clipboard security** - Generated passwords remain in clipboard indefinitely. Should auto-clear after 30-60 seconds for security.

9. **Password history** - No ability to view previously used passwords for a website or track when passwords were created/modified.

10. **Export/Import functionality** - Users cannot backup or migrate their password database to another machine.

11. **Master password protection** - No authentication required to access the application. Should implement a master password on startup.

12. **Password expiry warnings** - No notifications when passwords are old and should be changed (e.g., 90+ days old).

---
