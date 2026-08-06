words = ["activate","activation","reactivation"]

def parser(word):

    prefix=""
    suffix=""
    root="act"
    sequence=""
    meaning=""

    if word=="activate":
        suffix="-ivate"
        sequence="act → activate"
        meaning="Verb"

    elif word=="activation":
        suffix="-ivation"
        sequence="act → activate → activation"
        meaning="Noun"

    elif word=="reactivation":
        prefix="re-"
        suffix="-ivation"
        sequence="act → activate → activation → reactivation"
        meaning="Repeat activation"

    return [word,prefix,root,suffix,sequence,meaning,"act"]

print("{:<15}{:<8}{:<8}{:<12}{:<40}{:<20}{:<10}".format(
    "Word","Prefix","Root","Suffix","Sequence","Meaning","Normalized"))

for w in words:
    print("{:<15}{:<8}{:<8}{:<12}{:<40}{:<20}{:<10}".format(*parser(w)))