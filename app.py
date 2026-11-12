def greet():
    print("Welcome to DEVOPS LAB")

def login(username):
    if not username:
        print("Username is required")
        return
    print(f"User {username} logged in successfully")

def logout(username):
    print(f"User {username} logged out")

def signup(username):
    if not username:
        print("Username is required for signup")
        return
    print(f"User {username} registered successfully")

greet()
login("student1")
