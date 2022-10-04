# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

def shopping_cart():
    full_cart = []
    while True:


        carts = input("What would you like to do? add/remove/show/clear/quit ")
        if carts == "add":
            item = input("What would you like to add in your cart? ")
            price = input(f"What is the price of {item} ?")
            total = input(f"How many {item}'s would you like to add? ")
            print(f"{total} {item}'s have been added to your cart")

        elif carts == "remove":
            get_out = input(f"How many of the {total} {item}'s would you like to remove? ")
            print(f"{get_out} {item}'s have been removed from your cart")
            
        elif carts == "clear":
            you_sure = input("are you sure? Once you clear you cannot undo, Y/N ")
            if you_sure == "Y":
                full_cart.clear()
                print("Your cart has been cleared")
            else:
                continue
        elif carts == "quit":
            print("Thank you for shopping with us")
            print("your reciept: ")
            break

        while carts not in {"add", "remove", "show", "clear", "quit"}:
            carts = input("That's not a valid response. What would you like to do? add/remove/show/clear/quit ")
        # elif carts == "clear":
        #     put_back = input("What item would you like to remove in the cart? ")
        #     print(f"{put_back} is not in your cart")

#         elif carts == "quit":
#             put_back = input("What item would you like to remove in the cart? ")
#             print(f"{put_back} is not in your cart")
shopping_cart()