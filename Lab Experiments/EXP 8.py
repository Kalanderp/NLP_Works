import random
tag_dict = {
    "I": ["PRP"],
    "like": ["VB", "IN"],
    "apple": ["NN"],
    "can": ["MD", "NN"],
    "eat": ["VB"]
}
sentence = input("Enter sentence: ").split()
print("\nStochastic POS Tags:")
for word in sentence:
    if word in tag_dict:
        tag = random.choice(tag_dict[word])
    else:
        tag = "NN"
    print(word, "->", tag)