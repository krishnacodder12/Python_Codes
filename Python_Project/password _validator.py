import re

def password_validator(password):
    # Minimum length of the password
    min_length = 8
    
    # Check if the password meets the minimum length requirement
    if len(password) < min_length:
        return False, "Password should be at least {} characters long.".format(min_length)
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password should contain at least one uppercase letter."
    
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password should contain at least one lowercase letter."
    
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False, "Password should contain at least one digit."
    
    # Check if the password contains special characters (optional)
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password should contain at least one special character."
    
    # If all checks pass, the password is valid
    return True, "Password is valid."

# Example usage
password = input("Enter your password: ")
is_valid, message = password_validator(password)

if is_valid:
    print("Password is valid.")
else:
    print("Invalid password:", message)
