class ValueNotRecognised(Exception):
    # raised when the input is neither given options
    pass


def shopping():
    # Create a dictionary with a minimum of 3 items and prices
    # One of the items needs to cost more than £100
    shop_dict = {"Outdoor Coat": 150, "Thermal Leggings": 75, "Wooly Hat": 30, "Jumper": 45}
    # Customer’s available money is £100
    customer_wallet = 100
    # Welcome the customer and display the items and their prices,
    welcome_message = "Welcome to the Outdoor Shop, please find our available items and prices below:\n"
    print(welcome_message, shop_dict)
    # along with an option to “exit” accept the option as an input,
    try:
        to_shop = input("If you would like to shop, type 'YES', if not, type 'EXIT'.")
        if to_shop == "YES":
            purchase = True
            shopping = input("What would you like to buy?")
        elif to_shop == "EXIT":
            purchase = False
            print("Thanks for visiting! Come back soon!")
        else:
            # an invalid input should raise a ValueError
            raise ValueNotRecognised
    except:
        print("Please try again, using a valid input of either 'YES' or 'EXIT'.")


    customer_shopping_list = []
    # if the item is in the dict I want to put the item in the list
    while purchase:
        if shopping in shop_dict:
            customer_shopping_list.append(shopping)
            print(f"Processing transaction for {customer_shopping_list}... *beep beep beep*")
        print(f"This item costs £{shop_dict.get(shopping)} and you have £{customer_wallet}.")
        basket = shop_dict.get(shopping)
        break


    while purchase:
        purchase_attempts = 0
        if customer_wallet >= basket:
            # If the customer can afford it, print out a message saying “Here’s your {item}!”
            # The user should be then greeted out of the shop,
            print(f"Here is your ({customer_shopping_list}!", "Thank you for shopping with us, please come back soon!")
            break
        # If the customer cannot afford it, note the attempt and ask if they have more money
        elif customer_wallet < basket:
            purchase_attempts += 1
            more_money = input("Do you have some more money? YES/NO")
            # if they do and enter the amount it should be added to the balance
            if more_money == "YES":
                how_much = int(input("How much more money do you have?"))
                customer_wallet += how_much
                print(f"You have £{customer_wallet}")
                if customer_wallet >= basket:
                    print(f"Here is your ({customer_shopping_list}!",
                          "Thank you for shopping with us, please come back soon!")
                elif customer_wallet < basket:
                    purchase_attempts += 1
                    print("You still do not have enough money")
                    second_try = int(input("This is your second try, how much more money do you have?"))
                    customer_wallet += second_try
                    print(f"You now have £{customer_wallet}")
                    if customer_wallet > basket:
                        print(f"Here is your ({customer_shopping_list}!",
                              "Thank you for shopping with us, please come back soon!")
                    elif customer_wallet < basket:
                        purchase_attempts += 1
                        print("You still do not have enough money")
                        final_try = int(input("This is your final try, how much more money do you have?"))
                        customer_wallet += final_try
                        print(f"You now have £{customer_wallet}")
                        if customer_wallet >= basket:
                            print(f"Here is your ({customer_shopping_list}!",
                                  "Thank you for shopping with us, please come back soon!")

            elif more_money == "NO":
                print("Thanks for visiting, please come back again when you have sufficient funds.")
            break
    while purchase:
        try:
            # The purchase should be tried a maximum of 3 times
            if customer_wallet < basket and purchase_attempts >= 3:
                raise ValueNotRecognised
        # If it fails a custom error should be raised and the customer will exit the shop.
        except:
            print("\nYou have tried to purchase this item over 3 times and do not have sufficient funds for this item.\n",
                  "\nPlease come back another time when you have sufficient funds. Goodbye.")
        break


shopping()
