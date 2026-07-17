import re

products = [
    "Apple iPhone",
    "Apple Watch",
    "Samsung Galaxy",
    "Samsung TV",
    "Dell Laptop",
    "HP Laptop",
    "Lenovo Laptop",
    "Wireless Mouse",
    "Gaming Mouse",
    "Bluetooth Speaker",
    "Smart Watch",
    "Phone Charger"
]

def search_products(pattern, description, flags=0):
    matches = [product for product in products if re.search(pattern, product, flags)]

    print("\n" + "="*40)
    print(description)
    print("="*40)

    if matches:
        for product in matches:
            print(product)
    else:
        print("No matching products found.")

    print("Total Matches :", len(matches))
    return len(matches)

# Searches
exact = search_products(r"^Samsung Galaxy$", "1. Exact Keyword Search")
prefix = search_products(r"^Apple", "2. Prefix Search")
suffix = search_products(r"Laptop$", "3. Suffix Search")
partial = search_products(r"Mouse", "4. Partial Keyword Search")
case = search_products(r"watch", "5. Case-Insensitive Search", re.IGNORECASE)

# Report
print("\n========== SEARCH REPORT ==========")
print("Exact Keyword Matches :", exact)
print("Prefix Search Matches :", prefix)
print("Suffix Search Matches :", suffix)
print("Partial Keyword Matches :", partial)
print("Case-Insensitive Matches :", case)