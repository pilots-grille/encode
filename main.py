# main.py
from user import User

def main():
    user = User()
    user.create_user()
    user.save_user()

if __name__ == "__main__":
    main()
