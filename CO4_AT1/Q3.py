# Word Sense Disambiguation in E-Commerce Search Engines

# Search queries with possible senses
queries = {
    "Apple accessories": ["Fruit", "Technology Brand"],
    "Mouse wireless": ["Animal", "Computer Device"],
    "Java tutorial": ["Island", "Programming Language"],
    "Python course": ["Snake", "Programming Language"]
}

# Clicked results provide contextual information
clicked_results = {
    "Apple accessories": "iPhone Charger",
    "Mouse wireless": "Bluetooth Mouse",
    "Java tutorial": "Coding Lessons",
    "Python course": "Software Development Training"
}

# Context words associated with each possible sense
sense_keywords = {
    "Fruit": [
        "fruit", "food", "juice", "apple fruit"
    ],

    "Technology Brand": [
        "iphone", "charger", "mac", "ipad", "technology", "accessories"
    ],

    "Animal": [
        "animal", "rat", "pet", "rodent"
    ],

    "Computer Device": [
        "bluetooth", "computer", "wireless", "keyboard", "mouse"
    ],

    "Island": [
        "island", "travel", "tourism", "country", "vacation"
    ],

    "Programming Language": [
        "coding", "programming", "software", "development",
        "tutorial", "course", "lessons"
    ],

    "Snake": [
        "snake", "reptile", "animal", "wildlife"
    ]
}

print("=" * 70)
print("WORD SENSE DISAMBIGUATION IN E-COMMERCE")
print("=" * 70)

for query, possible_senses in queries.items():

    clicked = clicked_results[query].lower()

    scores = {}

    # Calculate contextual score for each possible sense
    for sense in possible_senses:

        score = 0

        for keyword in sense_keywords[sense]:

            if keyword in clicked:
                score += 1

        scores[sense] = score

    # Select sense with highest contextual score
    selected_sense = max(scores, key=scores.get)

    print("\nQuery:", query)
    print("Clicked Result:", clicked_results[query])
    print("Possible Senses:", possible_senses)
    print("Scores:", scores)
    print("Correct Sense:", selected_sense)

print("\n" + "=" * 70)
print("FINAL RESULTS")
print("=" * 70)

for query, possible_senses in queries.items():

    clicked = clicked_results[query].lower()

    scores = {}

    for sense in possible_senses:
        scores[sense] = sum(
            keyword in clicked
            for keyword in sense_keywords[sense]
        )

    selected_sense = max(scores, key=scores.get)

    print(f"{query:25} -> {selected_sense}")