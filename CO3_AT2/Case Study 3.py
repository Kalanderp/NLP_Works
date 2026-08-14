import math
words = ["economic", "growth", "increases", "employment"]
tags = ["JJ", "NN", "NNS", "NN"]
# Transformation-Based Tagging rule:
# Change NNS to VBZ if the preceding word is tagged NN.
for i in range(1, len(tags)):
 if tags[i] == "NNS" and tags[i - 1] == "NN":
    tags[i] = "VBZ"
print("Corrected tags:")
print(" ".join(f"{word}/{tag}" for word, tag in zip(words, tags)))
# Corpus-based frequency distribution
counts = {
 "economic": 120,
 "growth": 450,
 "increases": 210,
 "employment": 380
}
total = sum(counts.values())
probabilities = {}
for word, count in counts.items():
 probabilities[word] = count / total
 print(f"{word:12s} count={count:3d} probability={probabilities[word]:.5f}")
# Entropy of the word-frequency distribution
frequency_entropy = -sum(
 p * math.log2(p) for p in probabilities.values()
)
print("Frequency-distribution entropy =",
 round(frequency_entropy, 4), "bits")
# Illustrative tag uncertainty before and after a rule
before = {"NNS": 0.50, "VBZ": 0.50}
after = {"NNS": 0.05, "VBZ": 0.95}
def entropy(distribution):
 return -sum(p * math.log2(p) for p in distribution.values())
print("Illustrative entropy before rule =", round(entropy(before), 4))
print("Illustrative entropy after rule =", round(entropy(after), 4))