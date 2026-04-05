menu = {
    "espresso": 120,
    "cappuccino": 180,
    "latte": 200,
    "cold coffee": 220,
    "iced americano": 160,
    "masala chai": 100,
    
    "veg Sandwich": 150,
    "grilled Cheese Sandwich": 180,
    "veg Burger": 200,
    "french Fries": 120,
    "garlic Bread": 140,
    
    "white Sauce Pasta": 250,
    "red Sauce Pasta": 240,
    "veg Pizza Small": 300,
    "veg Pizza Medium": 450,
    "paneer Wrap": 220,
    
    "chocolate Cake": 180,
    "Brownie": 150,
    "Ice Cream": 120,
    "Cheesecake": 220
}

print("Menu:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

