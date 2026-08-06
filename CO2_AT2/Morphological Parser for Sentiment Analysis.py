words = ["disagree", "agreement", "agreeable"]

def parse(word):

    prefix = ""
    suffix = ""
    root = ""
    category = ""
    meaning = ""

    if word.startswith("dis"):
        prefix = "dis-"
        root = "agree"
        category = "Derivational"
        meaning = "Opposite of agree"

    elif word.endswith("ment"):
        suffix = "-ment"
        root = "agree"
        category = "Derivational"
        meaning = "State or act of agreeing"

    elif word.endswith("able"):
        suffix = "-able"
        root = "agree"
        category = "Derivational"
        meaning = "Capable of agreeing"

    return [word,prefix,root,suffix,category,meaning,"agree"]

print("{:<15}{:<10}{:<10}{:<10}{:<15}{:<30}{:<10}".format(
    "Word","Prefix","Root","Suffix","Category","Meaning","Normalized"))

for w in words:
    print("{:<15}{:<10}{:<10}{:<10}{:<15}{:<30}{:<10}".format(*parse(w)))