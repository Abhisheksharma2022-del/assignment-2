valid_username = "user1"
valid_password = "pass@123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == valid_username and password == valid_password:
    print("Authentication successful")

else:
    print("Authentication failed")