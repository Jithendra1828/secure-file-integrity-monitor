# 🔐 Secure File Integrity Monitoring System

A Python-based cybersecurity tool that detects unauthorized file modifications using SHA-256 cryptographic hashing.

---

## 📌 Overview

This project ensures file integrity by generating and storing SHA-256 hash values of files.
When the file is checked again, the system compares the current hash with the stored hash.

If any modification is detected:
- ⚠ The user is alerted
- 📝 The event is logged for auditing purposes

This project demonstrates real-world cybersecurity concepts such as integrity verification, logging, and modular architecture.

---

## 🏗 Project Architecture

### 📂 Project Structure

- main.py → Entry point of the application
- hash_utils.py → SHA-256 hash generation logic
- monitor.py → Monitoring, comparison, and logging logic
- data/ → Stores file hashes (hashes.json)
- logs/ → Stores monitoring logs (log.txt)
- test_files/ → Sample files for testing
- requirements.txt → Project dependencies
- .gitignore → Ignored files configuration

---

### ⚙ System Architecture

- Modular design separating hashing and monitoring logic
- Uses SHA-256 cryptographic hash function
- JSON-based persistent storage for file hashes
- Logging mechanism for audit tracking
- Error handling for missing or corrupted files

---

## ✨ Features

- 🛡 File-level monitoring
- 📂 Folder-level monitoring
- 🔐 SHA-256 cryptographic hashing
- 📝 Automatic logging system
- 🗂 JSON-based hash storage
- ⚠ Real-time modification detection (during execution)

---

## 🧠 Concepts Used

- Cryptographic Hash Functions (SHA-256)
- File Handling in Python
- OS Module for directory management
- Logging mechanisms
- Data Integrity Verification
- Defensive programming

---

## 🚀 How to Run

1. Navigate to the project folder:

   cd Secure-File-Integrity-Monitor

2. (Optional) Create Virtual Environment:

   python -m venv venv
   venv\Scripts\activate

3. Install Dependencies:

   pip install -r requirements.txt

4. Run the Application:

   python main.py

Enter the file or folder path when prompted.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Jithendra1828  
Cybersecurity & Python Developer
