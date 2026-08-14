import re
sentences = [
 "Book a flight ticket now.",
 "This book is interesting."
]
# Contextual rule-based tags for this case study
rule_based_tags = [
 [("Book", "VB"), ("a", "DT"), ("flight", "NN"),
 ("ticket", "NN"), ("now", "RB"), (".", ".")],
 [("This", "DT"), ("book", "NN"), ("is", "VBZ"),
 ("interesting", "JJ"), (".", ".")]
]
for sentence, tagged in zip(sentences, rule_based_tags):
 print("\n", sentence)
 print(" ".join(f"{word}/{tag}" for word, tag in tagged))
# Simplified HMM comparison for the word "book"
emission = {"VB": 0.6, "NN": 0.4}
transition_from_start = {"VB": 0.5, "NN": 0.5}
vb_likelihood = emission["VB"] * transition_from_start["VB"]
nn_likelihood = emission["NN"] * transition_from_start["NN"]
normalizer = vb_likelihood + nn_likelihood
print("\nP(book, VB) =", vb_likelihood)
print("P(book, NN) =", nn_likelihood)
print("Simplified P(VB | book) =", round(vb_likelihood / normalizer, 4))
print("Preferred tag =", "VB" if vb_likelihood > nn_likelihood else "NN")