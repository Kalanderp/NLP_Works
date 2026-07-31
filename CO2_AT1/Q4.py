words = ["writes", "writing", "written"]
print("{:<12}{:<35}{:<20}{:<18}{:<10}{:<15}".format(
    "Word", "State Transition", "Breakdown",
    "Pattern", "Root", "Normalized"))
print("-" * 120)
for word in words:
    if word == "writes":
        transition = "START -> write -> +s -> END"
        breakdown = "write + s"
        pattern = "Regular Inflection"
        root = "write"
    elif word == "writing":
        transition = "START -> write -> +ing -> END"
        breakdown = "write + ing"
        pattern = "Regular Inflection"
        root = "write"
    elif word == "written":
        transition = "START -> write -> irregular(en) -> END"
        breakdown = "write + en"
        pattern = "Irregular Inflection"
        root = "write"
    print("{:<12}{:<35}{:<20}{:<18}{:<10}{:<15}".format(
        word, transition, breakdown, pattern, root, root))