import os
from monitor import monitor_file, setup_environment

def main():
    print("\n🔐 === Secure File Integrity Monitoring System === 🔐\n")

    # Setup folders and required files
    setup_environment()

    path = input("📂 Enter file or folder path to monitor: ").strip()

    if os.path.isfile(path):
        monitor_file(path)

    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                monitor_file(full_path)

    else:
        print("❌ Invalid path provided.")

if __name__ == "__main__":
    main()
