import re
def validate_email(email):
    pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$'
    if re.match(pattern, password):
        return "Strong Password"
    else:
        return "Weak Password"
def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    if re.match(pattern, mobile):
        return "Valid Mobile Number"
    else:
        return "Invalid Mobile Number"
email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")
print(validate_email(email))
print(validate_password(password))
print(validate_mobile(mobile))
