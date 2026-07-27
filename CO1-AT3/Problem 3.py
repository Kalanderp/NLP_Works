import re
def search_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)
def search_phone(text):
    pattern = r'\b\d{10}\b'
    return re.findall(pattern, text)
def search_hashtag(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)
def search_mention(text):
    pattern = r'@\w+'
    return re.findall(pattern, text)
def search_prefix(text, prefix):
    pattern = r'\b' + re.escape(prefix) + r'\w*'
    return re.findall(pattern, text)
def search_suffix(text, suffix):
    pattern = r'\w*' + re.escape(suffix) + r'\b'
    return re.findall(pattern, text)
text = """Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing"""
while True:
    print("\nUser Menu")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Dates found:", search_date(text))
    elif choice == "2":
        print("Phone Numbers found:", search_phone(text))
    elif choice == "3":
        print("Hashtags found:", search_hashtag(text))
    elif choice == "4":
        print("Mentions found:", search_mention(text))
    elif choice == "5":
        prefix = input("Enter prefix: ")
        print("Words with prefix:", search_prefix(text, prefix))
    elif choice == "6":
        suffix = input("Enter suffix: ")
        print("Words with suffix:", search_suffix(text, suffix))
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")