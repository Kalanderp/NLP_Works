import re
from collections import Counter

# Corpus
corpus = [
    "The student is reading a book",
    "The student is writing an assignment",
    "The student is solving a problem",
    "The student is learning English",
    "The student is preparing a report",
    "The teacher is reading a book",
    "The teacher is checking the assignment",
    "The teacher is preparing a report",
    "The student likes the book"
]

# Tokenization
def tok(s):
    return re.findall(r"\b\w+\b", s.lower())


# Tokenize sentences
S = [tok(s) for s in corpus]

# Unigram counts
U = Counter(
    w for s in S for w in s
)

# Bigram counts
B = Counter(
    (s[i], s[i + 1])
    for s in S
    for i in range(len(s) - 1)
)

# Trigram counts
T = Counter(
    (s[i], s[i + 1], s[i + 2])
    for s in S
    for i in range(len(s) - 2)
)

# Vocabulary
V = set(U)

# Total number of words
N = sum(U.values())


# Unigram probability
def p1(w, leave=0):
    return max(U[w] - leave, 0) / max(N - leave, 1)


# Bigram probability
def p2(a, b, leave=0):
    return max(B[(a, b)] - leave, 0) / max(U[a] - leave, 1)


# Trigram probability
def p3(a, b, c, leave=0):
    return max(T[(a, b, c)] - leave, 0) / max(B[(a, b)] - leave, 1)


# Backoff model
def backoff(a, b, c):
    if T[(a, b, c)]:
        return p3(a, b, c)

    if B[(b, c)]:
        return p2(b, c)

    return p1(c)


# Deleted interpolation
weights = [0.0, 0.0, 0.0]

for (a, b, c), count in T.items():

    candidates = [
        p1(c, 1),
        p2(b, c, 1),
        p3(a, b, c, 1)
    ]

    best_index = candidates.index(max(candidates))
    weights[best_index] += count


# Calculate interpolation weights
total_w = sum(weights)

if total_w > 0:
    l1, l2, l3 = [w / total_w for w in weights]
else:
    l1, l2, l3 = 1 / 3, 1 / 3, 1 / 3


# Deleted interpolation probability
def deleted_interpolation(a, b, c):
    return (
        l1 * p1(c)
        + l2 * p2(b, c)
        + l3 * p3(a, b, c)
    )


# Find top predicted words
def top_words(query, method, k=5):

    w = tok(query)

    if len(w) < 2:
        return []

    a, b = w[-2], w[-1]

    scores = {}

    for c in V:

        if method == "unsmoothed":

            scores[c] = (
                p3(a, b, c)
                if T[(a, b, c)]
                else 0
            )

        elif method == "backoff":

            scores[c] = backoff(a, b, c)

        elif method == "deleted":

            scores[c] = deleted_interpolation(a, b, c)

        else:
            raise ValueError(
                "Invalid method. Use unsmoothed, backoff, or deleted."
            )

    return sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:k]


# Query
query = "The student is"


# Display deleted-interpolation weights
print("Deleted-interpolation weights:")
print("Lambda 1 =", l1)
print("Lambda 2 =", l2)
print("Lambda 3 =", l3)


# Display predictions
print("\nTop predictions:")

for method in ["unsmoothed", "backoff", "deleted"]:
    print(method, ":", top_words(query, method))


# Unseen trigram example
print("\nUnseen trigram example:")

print(
    "Unsmoothed =",
    p3("student", "is", "dancing")
)

print(
    "Backoff =",
    backoff("student", "is", "dancing")
)

print(
    "Interpolated =",
    deleted_interpolation("student", "is", "dancing")
)