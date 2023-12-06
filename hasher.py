# hasher.py
import hashlib

class Hasher:
    @staticmethod
    def hash_string(data):
        return hashlib.sha256(data.encode()).hexdigest()
