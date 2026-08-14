import re
import math
from collections import Counter

# Training data
train = [
    [
        ("the", "DT"),
        ("student", "NN"),
        ("reads", "VBZ"),
        ("a", "DT"),
        ("book", "NN")
    ],
    [
        ("the", "DT"),
        ("teacher", "NN"),
        ("checks", "VBZ"),
        ("the", "DT"),
        ("report", "NN")
    ],
    [
        ("a", "DT"),
        ("smart", "JJ"),
        ("student", "NN"),
        ("writes", "VBZ"),
        ("quickly", "RB")
    ],
    [
        ("the", "DT"),
        ("student", "NN"),
        ("solves", "VBZ"),
        ("a", "DT"),
        ("problem", "NN")
    ],
    [
        ("he", "PRP"),
        ("reads", "VBZ"),
        ("in", "IN"),
        ("the", "DT"),
        ("library", "NN")
    ],
    [
        ("the", "DT"),
        ("teacher", "NN"),
        ("and", "CC"),
        ("the", "DT"),
        ("student", "NN"),
        ("work", "VB"),
        ("together", "RB")
    ]
]


# Word-to-tag lexicon
tag_lexicon = {
    "the": "DT",
    "a": "DT",
    "an": "DT",

    "he": "PRP",
    "she": "PRP",
    "they": "PRP",
    "we": "PRP",

    "in": "IN",
    "on": "IN",
    "at": "IN",
    "with": "IN",
    "after": "IN",

    "and": "CC",
    "but": "CC",

    "smart": "JJ",
    "good": "JJ",

    "quickly": "RB",
    "slowly": "RB",

    "will": "MD",
    "can": "MD"
}


# Tokenization
def tokenize(s):
    return re.findall(r"\b\w+\b", s.lower())


# Rule-Based POS Tagger
def rule_tag(words):
    tags = []

    for i, w in enumerate(words):

        prev = tags[-1] if tags else None

        if w in tag_lexicon:
            tag = tag_lexicon[w]

        elif w.endswith("ly"):
            tag = "RB"

        elif w.endswith("ing"):
            tag = "VBG"

        elif w.endswith(("ed", "en")):
            tag = "VBN"

        elif prev in {"PRP", "MD", "VB", "VBP"}:
            tag = "VB"

        elif prev == "DT":
            tag = "NN"

        elif w.endswith(("s", "es")) and len(w) > 3:
            tag = "VBZ"

        else:
            tag = "NN"

        tags.append(tag)

    return tags


# Counters
emission = Counter()
tag_count = Counter()
transition = Counter()
tags = set()


# Train HMM model
for sent in train:

    prev = "<START>"

    for word, tag in sent:

        emission[(tag, word)] += 1
        tag_count[tag] += 1
        transition[(prev, tag)] += 1

        tags.add(tag)

        prev = tag


# Emission probability
def emit_p(tag, word):
    return (
        emission[(tag, word)] + 1
    ) / (
        tag_count[tag] + len(tags) + 1
    )


# Transition probability
def trans_p(prev, tag):

    denom = sum(
        c
        for (p, t), c in transition.items()
        if p == prev
    )

    return (
        transition[(prev, tag)] + 1
    ) / (
        denom + len(tags)
    )


# Viterbi algorithm
def viterbi(words):

    if not words:
        return []

    dp = [{}]
    back = [{}]

    # Initialization
    for tag in tags:

        dp[0][tag] = (
            math.log(trans_p("<START>", tag))
            + math.log(emit_p(tag, words[0]))
        )

        back[0][tag] = None

    # Recursion
    for i in range(1, len(words)):

        dp.append({})
        back.append({})

        for tag in tags:

            best_prev = None
            best_score = -float("inf")

            for prev in tags:

                score = (
                    dp[i - 1][prev]
                    + math.log(trans_p(prev, tag))
                    + math.log(emit_p(tag, words[i]))
                )

                if score > best_score:
                    best_prev = prev
                    best_score = score

            dp[i][tag] = best_score
            back[i][tag] = best_prev

    # Find best final tag
    last = max(
        dp[-1],
        key=dp[-1].get
    )

    result = [last]

    # Backtracking
    for i in range(len(words) - 1, 0, -1):

        result.append(
            back[i][result[-1]]
        )

    return list(reversed(result))


# Transformation-Based Tagging
def transform_tag(words, initial):

    tags = initial[:]

    for i, w in enumerate(words):

        if (
            i > 0
            and tags[i - 1] == "DT"
            and w not in tag_lexicon
        ):
            tags[i] = "NN"

        if (
            i > 0
            and tags[i - 1] in {"PRP", "MD"}
        ):
            tags[i] = "VB"

        if w.endswith("ly"):
            tags[i] = "RB"

    return tags


# Test sentence
sentence = "The student reads a book quickly"

words = tokenize(sentence)

# Rule-based tagging
rule = rule_tag(words)

# HMM / Stochastic tagging
hmm = viterbi(words)

# Transformation-based tagging
transformed = transform_tag(words, rule)


# Display results
print("Input:", sentence)

print(
    "Rule-Based:",
    list(zip(words, rule))
)

print(
    "Stochastic:",
    list(zip(words, hmm))
)

print(
    "Transformation-Based:",
    list(zip(words, transformed))
)