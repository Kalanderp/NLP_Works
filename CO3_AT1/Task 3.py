import re
import math
from collections import Counter

# Training data
train = [
    "the student reads a book",
    "the student writes a report",
    "the teacher reads a book",
    "the teacher checks a report",
    "the student solves a problem",
    "the teacher solves a problem"
]

# Test data
test = [
    "the student reads a report",
    "the teacher checks a book",
    "the student solves a problem"
]


# Tokenization function
def tok(s):
    return re.findall(r"\b\w+\b", s.lower())


# Tokenize training and test data
train_tok = [tok(s) for s in train]
test_tok = [tok(s) for s in test]


# Count unigrams
U = Counter(
    w for s in train_tok for w in s
)

# Count bigrams
B = Counter(
    (s[i], s[i + 1])
    for s in train_tok
    for i in range(len(s) - 1)
)

# Count trigrams
T = Counter(
    (s[i], s[i + 1], s[i + 2])
    for s in train_tok
    for i in range(len(s) - 2)
)


# Vocabulary
V = set(U)

V_size = len(V)

# Total number of words
N = sum(U.values())


# Probability function
def prob(word, context, n, smooth=True):

    # Unigram probability
    if n == 1:
        c = U[word]

        if smooth:
            return (c + 1) / (N + V_size)
        else:
            return c / N

    # Bigram probability
    elif n == 2:
        c = B[(context[-1], word)]
        d = U[context[-1]]

        if smooth:
            return (c + 1) / (d + V_size)
        else:
            return c / d if d else 0

    # Trigram probability
    elif n == 3:
        c = T[
            (context[-2], context[-1], word)
        ]

        d = B[
            (context[-2], context[-1])
        ]

        if smooth:
            return (c + 1) / (d + V_size)
        else:
            return c / d if d else 0

    else:
        raise ValueError("n must be 1, 2, or 3")


# Entropy calculation
def entropy(sentence, n):

    words = tok(sentence)

    total = 0.0
    surprises = []

    for i, w in enumerate(words):

        # Use unigram when there is insufficient history
        if n == 1 or i == 0:
            order = 1
            context = []

        # Use bigram when only one previous word is available
        elif n == 2 or i == 1:
            order = 2
            context = words[:i]

        # Use trigram when two previous words are available
        else:
            order = 3
            context = words[i - 2:i]

        # Calculate smoothed probability
        p = prob(
            w,
            context,
            order,
            smooth=True
        )

        # Calculate surprise
        surprise = -math.log2(p)

        total += surprise

        surprises.append(
            (w, surprise)
        )

    # Average entropy
    return total / len(words), surprises


# Calculate entropy for N = 1, 2, 3
for n in (1, 2, 3):

    values = []

    print(f"\nN = {n}")

    for s in test:

        h, detail = entropy(s, n)

        values.append(h)

        print(
            f"{s} -> entropy = {h:.3f} bits"
        )

    print(
        "Average entropy =",
        f"{sum(values) / len(values):.3f} bits"
    )


# Unsmoothed trigram probability
h = prob(
    "report",
    ["student", "reads"],
    3,
    smooth=False
)

print(
    "\nUnsmoothed P(report | student reads) =",
    h
)

if h == 0:
    print(
        "If probability is 0, -log2(P) is undefined/infinite."
    )


# Find highest and lowest surprise
all_surprises = []

for s in test:

    _, details = entropy(s, 3)

    for w, sp in details:
        all_surprises.append(
            (s, w, sp)
        )


highest = max(
    all_surprises,
    key=lambda x: x[2]
)

lowest = min(
    all_surprises,
    key=lambda x: x[2]
)


print(
    "\nHighest surprise:",
    highest
)

print(
    "Lowest surprise :",
    lowest
)