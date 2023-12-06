# file_manager.py
import json

class FileManager:
    @staticmethod
    def save_user_data(data):
        with open('users.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')
