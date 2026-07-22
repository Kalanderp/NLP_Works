def generate_plural(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"
nouns = ["cat", "dog", "box", "church", "baby", "bus"]
print("Singular -> Plural")
for word in nouns:
    print(word, "->", generate_plural(word))