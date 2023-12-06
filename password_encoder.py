# password_encoder.py
from hasher import Hasher

class PasswordEncoder:
    @staticmethod
    def encode_password(password_plain, salt):
        hashed_password = Hasher.hash_string(password_plain + salt)
        return hashed_password
