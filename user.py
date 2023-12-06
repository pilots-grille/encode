# user.py
from password_encoder import PasswordEncoder
from file_manager import FileManager
from salt_generator import SaltGenerator

class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.salt = None

    def create_user(self):
        self.username = input("Enter username: ")
        password_plain = input("Enter password: ")

        # Generate salt
        self.salt = SaltGenerator.generate_salt()

        # Hash the password with the salt
        self.password = PasswordEncoder.encode_password(password_plain, self.salt)

    def save_user(self):
        data = {
            'username': self.username,
            'password': self.password,
            'salt': self.salt
        }
        FileManager.save_user_data(data)
