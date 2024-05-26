menu = {
    'pizza': 130,
    'burger': 120,
    'salad': 100,
    'kattiroll': 100,
    'samosa': 30,
    'laudapau': 110,
}

print("Welcome To JOSHI Restaurant")
print("pizza: RS130\nburger: RS120\nsalad: RS100\nkattiroll: RS100\nsamosa: RS30\nlaudapau: RS110")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' is added to the order.")
else:
    print(f"Sorry, this item '{item_1}' is not available in our menu.")

another_order = input("Do you want to add another item? (yes/no)")
if another_order == "yes":
    
    item_2 = input("Enter the name of second item :")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' is added to the order.")
    else:
        print(f"Sorry, this item '{item_2}' is not available in our menu.")
else:
    print(f"Total amount of items to pay is {order_total}")