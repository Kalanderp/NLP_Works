import re

sentence = input("Enter sentence: ")
words = sentence.split()

print("\nRule-Based POS Tags:")

for word in words:
    if re.fullmatch(r".*ing", word):
        tag = "VBG"
    elif re.fullmatch(r".*ed", word):
        tag = "VBD"
    elif re.fullmatch(r".*ly", word):
        tag = "RB"
    elif word.lower() in ["a", "an", "the"]:
        tag = "DT"
    else:
        tag = "NN"

    print(word, "->", tag)