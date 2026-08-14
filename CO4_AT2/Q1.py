# CFG and PCFG Analysis for Banking Chatbot

import re

sentence = "Show me the transactions with the card from last month."

print("=" * 65)
print("BANKING CHATBOT - CFG / PCFG ANALYSIS")
print("=" * 65)

print("\nInput Sentence:")
print(sentence)

# Tokenization
tokens = re.findall(r"\b\w+\b", sentence.lower())

print("\nTokens:")
print(tokens)

# Possible interpretations
interpretations = {
    "Transactions from last month made with the card": 0.85,
    "Card from last month associated with transactions": 0.15
}

print("\nPossible Interpretations:")
for meaning, probability in interpretations.items():
    print(f"{meaning} -> Probability: {probability}")

# Select highest probability interpretation
best_interpretation = max(
    interpretations,
    key=interpretations.get
)

print("\nMost Probable Interpretation:")
print(best_interpretation)

print("\nPCFG Decision:")
print("The first interpretation is selected because it has the highest probability.")

# Feature structure example
features = {
    "Subject": {
        "Person": "Third",
        "Number": "Singular"
    },
    "Verb": {
        "Tense": "Present"
    }
}

print("\nFeature Structure:")
for item, values in features.items():
    print(item, ":", values)

print("\nEarley Parsing:")
print("Suitable for ambiguous, recursive and incomplete input.")

print("\nFinal Decision:")
print("Show transactions made with the card during last month.")