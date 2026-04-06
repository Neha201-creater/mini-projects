#Define the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':80,
    'Salad':70,
    'Coffee':100
    }
#greet
print('Welcome to PYTHON Restaurant')
print(" Pizza: Rs40\n Pasta: Rs50\n Burger: Rs80\n Salad: Rs70\n Coffee: Rs100")

order_total = 0
#80+70 = 150

item_1 = input(f"Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]#80+100
    print(f"Your item{item_1} has been added to your order")


else:
    print(f"Ordered item{item_1} is not available")  

another_order = input("Do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2}has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")
print(f"the total amount of items to pay is {order_total}")