import re

# Student Details
register_no = "24AIDS012"
email = "24aids012@sse.saveetha.edu.in"
course_code = "AIDS301"
semester = "5"
mobile = "8765432109"

status = True

# Register Number
if re.fullmatch(r"\d{2}[A-Z]{4}\d{3}", register_no):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    status = False

# Email
if re.fullmatch(r"[A-Za-z0-9._%+-]+@sse\.saveetha\.edu\.in", email):
    print("Email Address : Valid")
else:
    print("Email Address : Invalid")
    status = False

# Course Code
if re.fullmatch(r"[A-Z]{4}\d{3}", course_code):
    print("Course Code : Valid")
else:
    print("Course Code : Invalid")
    status = False

# Semester
if re.fullmatch(r"[1-8]", semester):
    print("Semester : Valid")
else:
    print("Semester : Invalid")
    status = False

# Mobile Number
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number : Valid")
else:
    print("Mobile Number : Invalid")
    status = False

# Final Report
print("\n========== Registration Report ==========")

if status:
    print("Registration Status : SUCCESSFUL")
else:
    print("Registration Status : FAILED")