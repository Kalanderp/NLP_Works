# First-Order Predicate Calculus for Smart Manufacturing

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

active = set()
maintenance = set()
producing = set()

# Apply predicate rules
for machine, status in machines.items():

    if status == "Active":
        active.add(machine)
        producing.add(machine)

    elif status == "Maintenance":
        maintenance.add(machine)

print("MACHINE STATUS")
print("-" * 40)

for machine, status in machines.items():
    print(machine, ":", status)

print("\nPREDICATE INFERENCE")
print("-" * 40)

print("Active Machines:", active)
print("Producing Machines:", producing)
print("Maintenance Machines:", maintenance)

# Additional production relationships
produces = {
    "M1": ["Gear"],
    "M2": ["Shaft"],
    "M3": ["Gear"],
    "M4": ["Bearing"]
}

available = []

for machine, products in produces.items():
    if machine in active:
        available.extend(products)

print("\nAVAILABLE PRODUCTS")
print("-" * 40)

for product in available:
    print(product)

print("\nGEAR PRODUCTION ANALYSIS")
print("-" * 40)

for machine, products in produces.items():

    if "Gear" in products:

        if machine in maintenance:
            print(
                machine,
                "is under maintenance, so its Gear production is affected."
            )

        elif machine in active:
            print(
                machine,
                "is active and producing Gear."
            )