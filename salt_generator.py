# salt_generator.py
import secrets

class SaltGenerator:
    @staticmethod
    def generate_salt():
        return secrets.token_hex(16)
