words=["create","creates","creating"]

def process(word):

    suffix=""
    grammar=""
    root="create"

    if word=="create":
        grammar="Base Form"

    elif word.endswith("s"):
        suffix="-s"
        grammar="Third Person Singular"

    elif word.endswith("ing"):
        suffix="-ing"
        grammar="Present Participle"

    return [word,suffix,grammar,root,"create"]

print("{:<15}{:<10}{:<25}{:<12}{:<12}".format(
    "Word","Suffix","Grammar","Root","Normalized"))

for w in words:
    print("{:<15}{:<10}{:<25}{:<12}{:<12}".format(*process(w)))