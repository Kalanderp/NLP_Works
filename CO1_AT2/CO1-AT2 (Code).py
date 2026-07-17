import re

# Sample text
text = """
Name: Rahul Sharma
Email: rahul.sharma@gmail.com
Phone: 9876543210
DOB: 15/07/2003
Website: https://www.google.com
PIN Code: 516269

Rahul is a Python Developer working in AI and Machine Learning.
"""

# Regular Expression Patterns
name_pattern = r"Name:\s*([A-Za-z ]+)"
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
phone_pattern = r"\b\d{10}\b"
date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"
url_pattern = r"https?://\S+"
pin_pattern = r"\b\d{6}\b"

# Information Extraction
name = re.search(name_pattern, text)
email = re.findall(email_pattern, text)
phone = re.findall(phone_pattern, text)
date = re.findall(date_pattern, text)
website = re.findall(url_pattern, text)
pin = re.findall(pin_pattern, text)

# Display Output
print("========== INFORMATION EXTRACTION ==========\n")

print("Name      :", name.group(1) if name else "Not Found")
print("Email     :", email)
print("Phone     :", phone)
print("DOB       :", date)
print("Website   :", website)
print("PIN Code  :", pin)