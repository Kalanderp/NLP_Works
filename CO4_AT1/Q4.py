# Syntax-Driven Semantic Analysis in Healthcare Information Systems

# Medical sentences
sentences = [
    "Doctor prescribed medicine to patient.",
    "Patient reported severe headache.",
    "Nurse monitored patient continuously.",
    "Medicine reduced blood pressure."
]

# Correct semantic roles for the given sentences
semantic_roles = {
    sentences[0]: {
        "Doctor": "Agent",
        "medicine": "Theme/Object",
        "patient": "Recipient"
    },

    sentences[1]: {
        "Patient": "Experiencer",
        "headache": "Symptom"
    },

    sentences[2]: {
        "Nurse": "Agent",
        "patient": "Patient/Theme"
    },

    sentences[3]: {
        "Medicine": "Cause",
        "blood pressure": "Affected Entity"
    }
}

# Roles originally given in the question
given_roles = {
    "Doctor": "Agent",
    "Medicine": "Instrument",
    "Patient": "Recipient",
    "Headache": "Symptom"
}

# Correct roles based on semantic analysis
correct_roles = {
    "Doctor": "Agent",
    "Medicine": "Theme/Object",
    "Patient": "Recipient",
    "Headache": "Symptom"
}

print("=" * 70)
print("SYNTAX-DRIVEN SEMANTIC ANALYSIS")
print("=" * 70)

# Display sentence-level semantic roles
for sentence in sentences:

    print("\nSentence:", sentence)
    print("-" * 70)

    for entity, role in semantic_roles[sentence].items():
        print(f"{entity:20} -> {role}")

# Validate the semantic roles
print("\n" + "=" * 70)
print("SEMANTIC ROLE VALIDATION")
print("=" * 70)

correct_count = 0
incorrect_count = 0

for entity in given_roles:

    given = given_roles[entity]
    correct = correct_roles[entity]

    if given == correct:

        print(
            f"{entity:15} | Given: {given:15} | "
            f"Correct: {correct:15} | VALID"
        )

        correct_count += 1

    else:

        print(
            f"{entity:15} | Given: {given:15} | "
            f"Correct: {correct:15} | ERROR"
        )

        incorrect_count += 1

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("Correct roles  :", correct_count)
print("Incorrect roles:", incorrect_count)

accuracy = (correct_count / len(given_roles)) * 100

print(f"Role Accuracy  : {accuracy:.2f}%")

print("\nMain Error:")
print("Medicine was incorrectly assigned the role 'Instrument'.")
print("Correct role: Theme/Object")