# Task 2: Inventory Management
inventory = {"Sugar": 50, "Milk": 80, "Bread": 40, "Rice": 100, "Soap": 60}

product = input("Enter product to check: ")
print(f"{product}: {inventory.get(product, 'not in stock')}")

inventory["Cooking Oil"] = 35   # add new product
inventory["Sugar"] = 70         # update quantity
del inventory["Soap"]           # remove a product

print("Final inventory:")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")
