import re

# Sample Resume
resume = """
Name: Priya Nair
Email: priya.nair@outlook.com
Mobile: +91 9845123670

Skills:
Python, Java, SQL, Machine Learning, NLP

Experience: 4 years

Worked as a Data Analyst.
"""

# Extract Name
name = re.search(r"Name\s*:\s*([A-Za-z ]+)", resume)
candidate_name = name.group(1) if name else "Not Found"

# Extract Email
email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)
candidate_email = email.group() if email else "Not Found"

# Extract Mobile Number
mobile = re.search(r"(\+91[- ]?)?[6-9]\d{9}", resume)
candidate_mobile = mobile.group() if mobile else "Not Found"

# Detect Skills
skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found_skills.append(skill)

# Extract Experience
experience = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)
years = int(experience.group(1)) if experience else 0

# Display Summary
print("========== Candidate Profile ==========")
print("Name :", candidate_name)
print("Email :", candidate_email)
print("Mobile :", candidate_mobile)
print("Skills :", ", ".join(found_skills))
print("Experience :", years, "Years")

# Eligibility Check
print("\nEligibility Status")
if years >= 2 and "Python" in found_skills:
    print(candidate_name, "is ELIGIBLE for Shortlisting.")
else:
    print(candidate_name, "is NOT ELIGIBLE.")