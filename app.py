def greet():
    print("Welcome to DEVOPS LAB")

def login(username):
    if not username:
        print("Username is required")
        return
    print(f"User {username} logged in successfully")

def logout(username):
    print(f"User {username} logged out")

greet()
login("student1")
