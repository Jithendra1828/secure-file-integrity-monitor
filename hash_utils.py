import hashlib

def generate_hash(file_path):
    """
    🔐 Generates SHA-256 hash of a file.
    Returns hexadecimal hash string.
    """

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None
