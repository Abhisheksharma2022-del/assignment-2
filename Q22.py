print("1. Login with Phone")
print("2. Login with Email")
print("3. Exit")

choice = input("Enter choice: ")

if choice == "1":
    phone = input("Enter phone number: ")
    otp = input("Enter OTP: ")

    if phone == "1234567890" and otp == "1234":
        print("Login successful with phone!")
    else:
        print("Invalid phone or OTP")

elif choice == "2":
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == "user@example.com" and password == "password123":
        print("Login successful with email!")
    else:
        print("Invalid email or password")

elif choice == "3":
    print("Exiting program...")

else:
    print("Invalid choice")