def greet():
    print("Welcome to DevOps Lab")

def login(username):
    if not username:
        print("Username is required")
        return
    print(f"User {username} logged in successfully")

greet()
login("student1")
