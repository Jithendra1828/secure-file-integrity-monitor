import os
import json
from datetime import datetime
from hash_utils import generate_hash

DATA_FOLDER = "data"
LOG_FOLDER = "logs"
HASH_FILE = os.path.join(DATA_FOLDER, "hashes.json")
LOG_FILE = os.path.join(LOG_FOLDER, "log.txt")


def setup_environment():
    """
    📁 Creates required folders and files if they don't exist.
    """
    os.makedirs(DATA_FOLDER, exist_ok=True)
    os.makedirs(LOG_FOLDER, exist_ok=True)

    # Create hashes.json if it doesn't exist
    if not os.path.exists(HASH_FILE):
        with open(HASH_FILE, "w") as f:
            json.dump({}, f)

    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("---- File Integrity Monitor Log ----\n")


def load_hashes():
    """
    📂 Loads stored file hashes safely.
    """
    try:
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_hashes(hashes):
    """
    💾 Saves updated hashes.
    """
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)


def log_event(message):
    """
    📝 Logs events with timestamp.
    """
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")


def monitor_file(file_path):
    """
    🔍 Monitors a file for changes using SHA-256 hashing.
    """
    hashes = load_hashes()
    current_hash = generate_hash(file_path)

    if current_hash is None:
        print(f"❌ File not found: {file_path}")
        return

    # 🔎 Display current hash for transparency
    print(f"🔎 Current SHA-256: {current_hash}")

    if file_path not in hashes:
        hashes[file_path] = current_hash
        save_hashes(hashes)
        print(f"✅ Now monitoring: {file_path}")
        log_event(f"{file_path} added to monitoring.")

    else:
        if hashes[file_path] == current_hash:
            print(f"🟢 SAFE: No changes detected → {file_path}")
        else:
            print(f"🚨 WARNING: File modified → {file_path}")
            log_event(f"{file_path} was modified.")
            hashes[file_path] = current_hash
            save_hashes(hashes)
