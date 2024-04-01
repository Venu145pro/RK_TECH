#python program to check password strength
#pwd=password variable
import re

def check_password_strength(pwd):
    # Minimum length check of password
    if len(pwd) < 8:
        return "Password must be at least 8 characters long."
    
    # Uppercase letter check
    if not re.search(r'[A-Z]', pwd):
        return "Password must contain at least one uppercase letter."
    
    # Lowercase letter check
    if not re.search(r'[a-z]', pwd):
        return "Password must contain at least one lowercase letter."
    
    # Digit check
    if not re.search(r'\d', pwd):
        return "Password must contain at least one digit."
    
    # Special character check
    if not re.search(r'[!@#$%^&*()-_=+]', pwd):
        return "Password must contain at least one special character."
    
    return "Password meets all the criteria for strength!.."

# Test the function
pwd = input("Enter your password: ")
result = check_password_strength(pwd)
print(result)