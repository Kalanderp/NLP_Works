words = ["played", "player", "playing"]
print("{:<12}{:<15}{:<10}{:<18}{:<12}".format(
    "Word", "Removed Affix", "Stem",
    "Transformation", "Normalized"))
print("-" * 75)
for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        t = "Inflectional"
    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        t = "Inflectional"
    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"
    else:
        stem = word
        affix = "-"
        t = "-"
    print("{:<12}{:<15}{:<10}{:<18}{:<12}".format(
        word, affix, stem, t, stem))