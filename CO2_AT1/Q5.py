from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["relational", "relation", "relate"]
print("{:<15}{:<35}{:<20}{:<15}".format(
    "Original Word",
    "Applied Rule",
    "Intermediate Form",
    "Final Stem"))
print("-" * 90)
for word in words:
    if word == "relational":
        rule = "Remove -ational, then remove e"
        intermediate = "relate"
    elif word == "relation":
        rule = "Remove -ion"
        intermediate = "relat"
    elif word == "relate":
        rule = "Remove final e"
        intermediate = "relat"
    stem = ps.stem(word)
    print("{:<15}{:<35}{:<20}{:<15}".format(
        word, rule, intermediate, stem))