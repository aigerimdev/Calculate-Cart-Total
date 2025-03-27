
def calculate_total(cart):
    prices = {
    "apple": 0.75,
    "beans": 2.00,
    "cheese": 2.50,
    "chicken": 4.00,
    "flour": 1.75,
    "onion": 0.50,
    "orange": 0.85,
    "lettuce": 1.25,
    "milk": 3.00,
    "tomato": 0.45
}
    total = 0.0
    
    if not cart:
        return 0.0
    
    for item in cart:
        item = item.lower()
        if item in prices:
            total += prices[item]
    return total


# print(calculate_total(["Tomato", "Tomato", "Tomato"]))
# print(calculate_total(["tomato"]))  # Banana not in prices
# print(calculate_total(["tomato"]))  # Will not match "Tomato"
# print(calculate_total(["tomato"]))  # Will not match "Tomato"
# print(calculate_total(["Tomato"] * 1000))  # Check performance and total
# print(calculate_total([123, None, "Apple"]))  # Should ignore or raise error

# print(calculate_total(["Unknown"]))  # Should ignore or raise error?
# print(calculate_total(["Tomato", "Apple", "Tomato"]))  # Sum twice for Tomato
# [("Apple", 2), ("Tomato", -1)] # Invalid

