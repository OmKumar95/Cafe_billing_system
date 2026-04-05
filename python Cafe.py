
print("Welcome to our cafe!")
print("Here is our menu:")
print("-------------------")


from Menu import menu
orders = {}
total = 0
print(" place your order")
order = input().strip().lower()
#print(f"You have ordered: {order}")

while order != "done" and order != "exit":
    if order in menu:
        print(f"You have ordered: {order} which costs ₹{menu[order]}")
        choice = input("Do you want to add this item to your order? (yes/no) ").strip().lower()
        if choice in ["yes", "y"]:
            total += menu[order]
            
            if order in orders:
                orders[order] += 1
            else:
                orders[order] = 1

            print(f"{order} has been added to your order.") 
        else: print(f"{order} has not been added to your order.")
    else:
        print(f"Sorry, {order} is not available in our menu.")
    
    order = input(" Anything else? (Type 'done' and 'exit' to finish your order) ").strip().lower()
print("\nYour order summary:")
for item, quantity in orders.items():
    price = menu[item] * quantity
    print(f"{item} x {quantity} - ₹{price}")

print(f"\n Total bill: ₹{total}\n")


print("Thank you for visiting our cafe!\n have a great day!")

