import re
text = "My email is Kalander123@gmail.com and my phone number is 98765**516."
email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
phone = re.search(r'\b\d{10}\b', text)
if email:
    print("Email Found:", email.group())
if phone:
    print("Phone Number Found:", phone.group())
words = re.findall(r'\bK\w*', text, re.IGNORECASE)
print("Words starting with 'K':", words)
