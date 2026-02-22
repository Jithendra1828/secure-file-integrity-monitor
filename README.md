# 🔐 Secure File Integrity Monitoring System

## 📌 Overview
This project detects unauthorized file modifications using SHA-256 cryptographic hashing.

It ensures file integrity by comparing stored hashes with current hashes.  
If any change is detected, the system alerts the user and logs the event for auditing.

---

## 🏗 Project Architecture

### 📂 Project Structure
- `main.py` → Entry point of the application  
- `hash_utils.py` → Handles SHA-256 hash generation  
- `monitor.py` → Monitoring, comparison & logging logic  
- `data/` → Stores file hashes (`hashes.json`)  
- `logs/` → Stores monitoring logs (`log.txt`)  

### ⚙ System Architecture
- Modular design with separation of hashing and monitoring logic  
- Uses SHA-256 cryptographic hash function  
- JSON-based persistent storage for hashes  
- Logging system for audit tracking  
- Error handling for corrupted or missing files  

---

## ✨ Features
- 🛡 File-level monitoring  
- 📂 Folder-level monitoring  
- 🔐 SHA-256 cryptographic hashing  
- 📜 Automatic logging system  
- 🗂 JSON-based hash storage  
- ⚠ Real-time modification detection (on execution)  

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
