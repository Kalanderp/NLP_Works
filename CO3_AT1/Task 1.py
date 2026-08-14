import re
from collections import Counter

# Corpus
corpus = [
    "The student is reading a book",
    "The student is writing an assignment",
    "The student is solving a problem",
    "The student is learning English",
    "The student is preparing a report",
    "The student is working hard",
    "The teacher is reading a book",
    "The teacher is checking the assignment",
    "The student likes the book"
]

# Tokenization function
def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

# Tokenize all sentences
sentences = [tokenize(s) for s in corpus]

# Count unigrams
unigram = Counter(
    word for sentence in sentences for word in sentence
)

# Count bigrams
bigram = Counter(
    (sentence[i], sentence[i + 1])
    for sentence in sentences
    for i in range(len(sentence) - 1)
)

# Count trigrams
trigram = Counter(
    (sentence[i], sentence[i + 1], sentence[i + 2])
    for sentence in sentences
    for i in range(len(sentence) - 2)
)

# Prediction function
def predict(query, n, k=5):
    words = tokenize(query)

    # Unigram prediction
    if n == 1:
        total = sum(unigram.values())

        scores = {
            word: count / total
            for word, count in unigram.items()
        }

    # Bigram prediction
    elif n == 2:
        if not words:
            return []

        last_word = words[-1]
        denominator = unigram[last_word]

        if denominator:
            scores = {
                b: count / denominator
                for (a, b), count in bigram.items()
                if a == last_word
            }
        else:
            scores = {}

    # Trigram prediction
    elif n == 3:
        if len(words) < 2:
            return []

        context = tuple(words[-2:])
        denominator = bigram[context]

        if denominator:
            scores = {
                t: count / denominator
                for (a, b, t), count in trigram.items()
                if (a, b) == context
            }
        else:
            scores = {}

    else:
        raise ValueError("n must be 1, 2, or 3")

    # Return top-k predictions
    return sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:k]


# Query
query = "The student is"

# Display predictions
for n in (1, 2, 3):
    print(f"\nN = {n}")
    print("Top predictions:", predict(query, n))


# Trigram probability
print("\nFrequency / probability for trigram ('the', 'student', 'is'):")

c = trigram[("the", "student", "is")]
d = bigram[("the", "student")]

print("count =", c)

if d:
    print("probability =", c / d)
else:
    print("probability = 0")


# Unseen trigram probability
print("\nUnseen trigram probability:")
print(trigram[("student", "is", "dancing")])