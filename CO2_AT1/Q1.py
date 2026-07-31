words = ["connected", "connecting", "connection"]
print("{:<15}{:<10}{:<10}{:<15}{:<20}{:<15}".format(
    "Word", "Root", "Suffix", "Type", "Parsed Structure", "Normalized"))
print("-" * 90)
for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        mtype = "Inflectional"
    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        mtype = "Inflectional"
    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        mtype = "Derivational"
    else:
        root = word
        suffix = "-"
        mtype = "-"
    print("{:<15}{:<10}{:<10}{:<15}{:<20}{:<15}".format(
        word, root, suffix, mtype, root + " + " + suffix, root))
