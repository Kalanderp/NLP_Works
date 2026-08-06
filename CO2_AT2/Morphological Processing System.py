words = ["analyzing", "analysis", "analytical"]

def analyze(word):
    result = {
        "Original": word,
        "Root": "",
        "Affix": "",
        "Type": "",
        "Normalized": "analyze"
    }

    if word.endswith("ing"):
        result["Root"] = "analyze"
        result["Affix"] = "-ing"
        result["Type"] = "Inflectional"

    elif word.endswith("sis"):
        result["Root"] = "analyze"
        result["Affix"] = "-sis"
        result["Type"] = "Derivational"

    elif word.endswith("ical"):
        result["Root"] = "analyze"
        result["Affix"] = "-ical"
        result["Type"] = "Derivational"

    return result

print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
    "Original","Root","Affix","Type","Normalized"))

for w in words:
    r = analyze(w)
    print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
        r["Original"],
        r["Root"],
        r["Affix"],
        r["Type"],
        r["Normalized"]))