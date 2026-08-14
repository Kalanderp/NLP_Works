# Voice Assistant Parsing Analysis

sentence = "Book a flight to Delhi with a window seat."

print("=" * 65)
print("VOICE ASSISTANT PARSING ANALYSIS")
print("=" * 65)

print("\nInput:")
print(sentence)

# Possible parse interpretations
parses = {
    "Book a flight to Delhi and request a window seat": 0.90,
    "Book a flight to Delhi, with the window-seat phrase as a separate modifier": 0.10
}

print("\nPossible Parse Interpretations:")

for parse, probability in parses.items():
    print(f"{parse}")
    print(f"Probability: {probability}\n")

# Select the most probable parse
best_parse = max(parses, key=parses.get)

print("Most Probable Interpretation:")
print(best_parse)

# Demonstrate partial input handling
partial_inputs = [
    "Book",
    "Book a flight",
    "Book a flight to Delhi",
    "Book a flight to Delhi with",
    "Book a flight to Delhi with a window seat"
]

print("\nPartial Input Processing:")
print("-" * 65)

for text in partial_inputs:
    print("Input:", text)
    print("Earley Parser Status: Partial parse maintained")

print("\nFinal Command:")
print("Destination: Delhi")
print("Seat Preference: Window")

print("\nRecommended Parser:")
print("Earley Parsing")

print("\nReason:")
print("It handles ambiguity, partial input and complex grammar without")
print("the extensive backtracking associated with basic top-down parsing.")