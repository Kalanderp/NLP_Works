words = ["unhappy", "happiness", "happily"]
print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<25}{:<10}".format(
    "Word", "Prefix", "Root", "Suffix",
    "Type", "Morphological Breakdown", "Normalized"))
print("-" * 100)
for word in words:
    prefix = "-"
    suffix = "-"
    root = word
    mtype = "Derivational"
    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
    elif word.endswith("ness"):
        suffix = "ness"
        root = word[:-4]
        if root.endswith("i"):
            root = root[:-1] + "y"
    elif word.endswith("ly"):
        suffix = "ly"
        root = word[:-2]
        if root.endswith("i"):
            root = root[:-1] + "y"
    breakdown = ""
    if prefix != "-":
        breakdown = prefix + " + " + root
    else:
        breakdown = root + " + " + suffix
    print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<25}{:<10}".format(
        word, prefix, root, suffix, mtype, breakdown, root))