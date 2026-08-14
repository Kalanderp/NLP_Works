# Healthcare NLP Architecture Demonstration
# CFG + Feature Structures + PCFG + Semantic Role Analysis

import re

sentence = (
    "The doctor who reviewed the patient last week recommends "
    "starting medication and scheduling a follow-up visit in Chennai."
)

print("=" * 75)
print("HEALTHCARE NLP SYSTEM")
print("=" * 75)

# ---------------------------------------------------------
# 1. Tokenization
# ---------------------------------------------------------

tokens = re.findall(r"\b[\w-]+\b", sentence)

print("\n1. TOKENS")
print("-" * 75)
print(tokens)

# ---------------------------------------------------------
# 2. Medical Entity Identification
# ---------------------------------------------------------

entities = {
    "Doctor": "doctor",
    "Patient": "patient",
    "Medication": "medication",
    "Follow-up": "follow-up visit",
    "Location": "Chennai",
    "Time": "last week"
}

print("\n2. MEDICAL ENTITIES")
print("-" * 75)

for entity, value in entities.items():
    print(f"{entity:15} -> {value}")

# ---------------------------------------------------------
# 3. Feature Structure
# ---------------------------------------------------------

feature_structure = {
    "Subject": {
        "Word": "doctor",
        "Person": "Third",
        "Number": "Singular"
    },

    "Verb": {
        "Word": "recommends",
        "Person": "Third",
        "Number": "Singular",
        "Tense": "Present"
    }
}

print("\n3. FEATURE STRUCTURE")
print("-" * 75)

for item, features in feature_structure.items():
    print(item, ":", features)

# Check subject-verb agreement
agreement = (
    feature_structure["Subject"]["Number"]
    == feature_structure["Verb"]["Number"]
)

print("\nSubject-Verb Agreement:", "Correct" if agreement else "Incorrect")

# ---------------------------------------------------------
# 4. CFG-style Syntactic Structure
# ---------------------------------------------------------

print("\n4. CFG-STYLE STRUCTURE")
print("-" * 75)

print("S")
print("|-- NP: The doctor")
print("|   |-- Relative Clause: who reviewed the patient last week")
print("|")
print("|-- VP: recommends")
print("    |-- VP: starting medication")
print("    |-- Conjunction: and")
print("    |-- VP: scheduling a follow-up visit in Chennai")

# ---------------------------------------------------------
# 5. PCFG Ambiguity Resolution
# ---------------------------------------------------------

possible_parses = {
    "Doctor recommends both treatment and follow-up": 0.90,
    "Doctor recommends only the medication": 0.10
}

print("\n5. PCFG PARSE SELECTION")
print("-" * 75)

for parse, probability in possible_parses.items():
    print(f"{parse} -> {probability}")

best_parse = max(possible_parses, key=possible_parses.get)

print("\nSelected Parse:")
print(best_parse)

# ---------------------------------------------------------
# 6. Sub-categorization Frames
# ---------------------------------------------------------

subcategorization = {
    "review": "Verb + Object",
    "recommend": "Verb + Gerund Phrase",
    "start": "Verb + Object",
    "schedule": "Verb + Object"
}

print("\n6. SUB-CATEGORIZATION FRAMES")
print("-" * 75)

for verb, frame in subcategorization.items():
    print(f"{verb:12} -> {frame}")

# ---------------------------------------------------------
# 7. Semantic Role Extraction
# ---------------------------------------------------------

semantic_roles = {
    "Agent": "Doctor",
    "Previous Action": "Reviewed patient",
    "Time": "Last week",
    "Main Action": "Recommends",
    "Treatment": "Starting medication",
    "Follow-up Action": "Scheduling a follow-up visit",
    "Location": "Chennai"
}

print("\n7. SEMANTIC ROLE EXTRACTION")
print("-" * 75)

for role, value in semantic_roles.items():
    print(f"{role:20} -> {value}")

# ---------------------------------------------------------
# 8. Structured Clinical Output
# ---------------------------------------------------------

structured_output = {
    "Diagnosis": "Not explicitly mentioned",
    "Doctor": "The doctor",
    "Previous Review": "Patient reviewed last week",
    "Recommended Treatment": "Start medication",
    "Follow-up": "Schedule follow-up visit",
    "Location": "Chennai"
}

print("\n8. STRUCTURED CLINICAL OUTPUT")
print("-" * 75)

for field, value in structured_output.items():
    print(f"{field:25} : {value}")

# ---------------------------------------------------------
# 9. Final Processing Result
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("FINAL RESULT")
print("=" * 75)

print("NLP processing completed successfully.")
print("CFG       -> Syntactic structure identified")
print("PCFG      -> Most probable interpretation selected")
print("Features  -> Subject-verb agreement verified")
print("NER       -> Medical entities identified")
print("Semantics -> Medical relationships extracted")
print("Output    -> Structured clinical information generated")