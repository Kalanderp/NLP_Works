words = ["govern","government","governance"]

def normalize(word):

    affix = ""
    level = ""
    root = "govern"

    if word == "govern":
        level = "Level 0"

    elif word.endswith("ment"):
        affix = "-ment"
        level = "Level 1"

    elif word.endswith("ance"):
        affix = "-ance"
        level = "Level 1"

    return [word,root,affix,level,"govern"]

print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
    "Word","Root","Affix","Hierarchy","Normalized"))

for w in words:
    print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(*normalize(w)))