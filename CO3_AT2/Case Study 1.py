import math
corpus = "data science is powerful data science drives innovation data science is evolving"
tokens = corpus.lower().split()
# Count unigrams and bigrams
unigram = {}
bigram = {}
for word in tokens:
 unigram[word] = unigram.get(word, 0) + 1
for first, second in zip(tokens, tokens[1:]):
 bigram[(first, second)] = bigram.get((first, second), 0) + 1
# Bigram MLE: P(science | data)
p_science_given_data = bigram[("data", "science")] / unigram["data"]
print("P(science | data) =", round(p_science_given_data, 4))
# Backoff estimate for unseen "improves" using add-one smoothing
vocabulary = set(tokens) | {"improves"}
V = len(vocabulary)
N = len(tokens)
p_improves = (unigram.get("improves", 0) + 1) / (N + V)
backoff_sequence = p_science_given_data * p_improves
print("Backoff P(improves) =", round(p_improves, 6))
print("Backoff sequence estimate =", round(backoff_sequence, 6))
# Deleted interpolation for P(is | data, science)
lambda_trigram = 0.5
lambda_bigram = 0.3
lambda_unigram = 0.2
p_trigram = 2 / 3 # supplied observed continuation estimate
p_bigram = 2 / 3
p_unigram = unigram["is"] / N
p_interpolated = (lambda_trigram * p_trigram +
 lambda_bigram * p_bigram +
 lambda_unigram * p_unigram)
p_data_science_is = (unigram["data"] / N) * p_science_given_data * p_interpolated
print("Interpolated P(is) =", round(p_interpolated, 4))
print("P(data science is) =", round(p_data_science_is, 4))
# Entropy of the two keyboard suggestions
probabilities = [0.66, 0.33]
entropy = -sum(p * math.log2(p) for p in probabilities)
print("Entropy =", round(entropy, 4), "bits")