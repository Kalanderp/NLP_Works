sentence = input("Enter sentence: ").split()

print("\nTransformation-Based POS Tags:")

for word in sentence:
    tag = "NN"
    if word.lower() in ["is", "am", "are", "was", "were"]:
        tag = "VB"
    elif word.endswith("ing"):
        tag = "VBG"
    elif word.endswith("ed"):
        tag = "VBD"
    elif word.lower() in ["the", "a", "an"]:
        tag = "DT"

    print(word, "->", tag)