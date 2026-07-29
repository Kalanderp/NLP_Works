import random
text = "I love python programming because python is easy to learn"
words = text.split()
bigrams = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    if word not in bigrams:
        bigrams[word] = []

    bigrams[word].append(next_word)
current = "I"
sentence = [current]

for i in range(8):
    if current in bigrams:
        current = random.choice(bigrams[current])
        sentence.append(current)
    else:
        break

print("Generated Text:")
print(" ".join(sentence))