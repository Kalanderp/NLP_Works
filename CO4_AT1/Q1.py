# Semantic Representation in Customer Support Chatbots

semantic_data = {
    "Activate international roaming": ("ACTIVATE", "Roaming"),
    "Deactivate caller tune": ("DEACTIVATE", "CallerTune"),
    "Check data balance": ("QUERY", "DataBalance"),
    "Enable 5G service": ("ACTIVATE", "5GService")
}

print("SEMANTIC REPRESENTATIONS")
print("-" * 50)

for query, (action, obj) in semantic_data.items():
    print("Query:", query)
    print("Action:", action)
    print("Object:", obj)
    print("Representation:", f"{action}({obj}, Customer)")
    print()

# Actual and predicted intents
intent_data = {
    "Q1": ("Activate Roaming", "Activate Roaming"),
    "Q2": ("Deactivate Caller Tune", "Activate Caller Tune"),
    "Q3": ("Check Data Balance", "Query Data Balance"),
    "Q4": ("Enable 5G Service", "Activate 5G Service")
}

print("INTENT ANALYSIS")
print("-" * 50)

for qid, (actual, predicted) in intent_data.items():

    # Treat semantically equivalent words as correct
    equivalent = {
        ("Check Data Balance", "Query Data Balance"),
        ("Enable 5G Service", "Activate 5G Service")
    }

    if actual == predicted or (actual, predicted) in equivalent:
        result = "Correct"
    else:
        result = "Error"

    print(qid, ":", result)
    print("Actual   :", actual)
    print("Predicted:", predicted)
    print()

print("Semantic Error: Q2")