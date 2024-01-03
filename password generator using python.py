import string
import random

def generate_password(length=8):
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using the random choice method
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Ask user if they want to specify password length
choice = input("Do you want to specify password length? (yes/no): ")

if choice.lower() == "yes":
    # Ask for password length
    while True:
        try:
            password_length = int(input("Enter the password length (6 to 64): "))
            if 6 <= password_length <= 64:
                break
            else:
                print("Password length must be between 6 and 64.")
        except ValueError:
            print("Please enter a valid number.")

    # Generate the password
    generated_password = generate_password(password_length)
else:
    # Generate the password using the default length
    generated_password = generate_password()

print("Generated Password:", generated_password)
