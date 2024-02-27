# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}


# ==============================================================================
# Functions
# ==============================================================================


def add_whitespace( input_string, total_string_length ) : 
    
    # Preceeding is a variable that denotes whether the whitespace
    # "preceeds" the string or follows the string.  Follow is default.
    preceeding = False 
    input_string = str(input_string)

    # To reduce the number of function inputs, I made it so a negative number 
    # would result in a right justified whitespace padding. (preceeding)
    if total_string_length < 0 : 
        total_string_length = total_string_length * -1
        preceeding = True

    number_of_spaces = total_string_length - len(input_string)

    if preceeding == True : 
        return (" " * number_of_spaces) + input_string
    else : 
        return input_string + (" " * number_of_spaces)


def print_menu_item( item_number, item_name, item_price ) :
    x = add_whitespace(item_number, -6)
    y = add_whitespace(item_name.title(), 24)
    z = add_whitespace(item_price, -5)
    print(f"{x} | {y} | ${z}")

# The get_menu_input funtion displays a menu to the user and asks for a choice
# It has two inputs, the "menu" data structure itself, and "menu type" which
# is basically a selector to determine which menu to show, main menu or the 
# specific menus.  It will then return a dictionary with three elements:
# name, price, and type.  These three elements are enough to determine
# what the user selected.
def get_menu_input( menu_data, menu_type ) :
    
    item_number = 0
    listed_items = []

    # The main menu will be a little different in appearance than the actual
    # menu items display.
    if menu_type.title() == "Main" :
        print(f"\nMenu # | Menu Category")
        print("------ | ---------------------------------")

        # For every key in the menu_data dictonary, print it out
        # with an associated item number.
        for category in menu_data.keys() : 
            x = add_whitespace(item_number, -6)
            y = add_whitespace(category.title(), 24)
            print(f"{x} | {y}")

            # I chose to append them to a list and leverage the list accessor
            # to keep track of the count.
            listed_items.append({"name": category, "price": 0, "type": "main menu choice"})
            item_number = item_number + 1


    # Print the specific menu requested by the customer
    elif menu_type.title() in menu_data :
        
        print(f"\n{menu_type.title()} Items:")
        print("Item # | Item name                | Price ")
        print("------ | ------------------------ | ------")

        # Print out every item in the sub menu
        for item_name,item_price in menu_data[menu_type].items() : 

            # If the item price is a float, we know it's a single item.
            if type(item_price) == float : 

                print_menu_item(item_number, item_name, item_price)

                # Add the item to a numbered list, just so we can track
                # what number and return the necessary info when the function is
                # done.
                listed_items.append({"name":item_name, 
                                     "price":item_price,
                                     "type":menu_type}) 
                item_number = item_number + 1

            # If the item price is a dictionary type, we know we need to print
            # the "sub items".  I chose to make the dictionary data structure
            # mostly transparent by concatinating the item and sub item into 
            # one line.          
            elif type(item_price) == dict : 

                for sub_item_name, sub_item_price in item_price.items() :
                    print_menu_item(item_number, item_name+" - "+sub_item_name, sub_item_price)
                    listed_items.append({"name":item_name + " - " + sub_item_name, 
                                         "price":sub_item_price,
                                         "type":menu_type}) 

                    item_number = item_number + 1

    print()

    choice = False
    
    while not choice : 

        choice = input( "Select an item number, M for Main Menu, C to check out, or Q to quit: ")

        if choice.upper() == "M" : 
            return {"name":"Main", "price":0.0, "type":"Main"}
        
        elif choice.upper() == "C" : 
            return {"name":"Checkout", "price":0.0, "type":"Checkout"}

        elif choice.upper() == "Q" : 
            return {"name":"Exit", "price":0.0, "type":"Exit"}

        elif choice.isdigit() :
            if int(choice) < len(listed_items) and int(choice) >= 0 :
                return listed_items[int(choice)]
            else : 
                print("Error: Unknown menu selection!")
                choice = False # This forces the choice selector to ask again.

        else : 
            print("Error: Unknown menu selection!")
            choice = False # This forces the choice selector to ask again.

def print_total_order(order) :

    total_price = 0

    print()
    print("-= Your Final Order =-")
    print()
    print(" Qty | Item                           | Price    ")
    print("---- | ------------------------------ | -------- ")

    # Go through the list of items they selected to buy, print each one out.
    for item in order :
        x = add_whitespace(item["quantity"], -4)
        y = add_whitespace(str(item["name"]).title(), 30)
        z = add_whitespace(item["price"], -7)
        print(f"{x} | {y} | ${z}")

        # Need to calculate the total price by multiplying the quanity by the price
        total_price = (float(item["price"]) * float(item["quantity"])) + float(total_price)
    
    a = add_whitespace("Total Price", -37)
    b = add_whitespace(total_price, -7)

    print("------------------------------------------------ ")
    print(f"{a} | ${b}")
    print()


# ==============================================================================
# MAIN PROGRAM BODY
# ==============================================================================


print("\nWelcome to the Variety Food Truck!\n==================================")

# Setting the initially selected menu
selection = "Main"

selected_menu_items = []

while True : 

    # Show the user a menu, ask for their selection, record their response.
    user_input = get_menu_input( menu, selection )

    # If the user selects Main, we set the next menu to Main.
    if user_input["type"] == "Main" :
        selection = "Main"

    # If the user selects something on the main menu, they selected
    # a submenu choice, and so we have to send them to the submenu.
    elif user_input["type"] == "main menu choice" :
        selection = user_input["name"]

    # If the user selected Exit, we need to drop out of the program.
    elif user_input["type"] == "Exit" :
        print("User selected exit")
        exit()

    # If the user selected Checkout, we'll display the total order
    # with total price and everything they selected.
    elif user_input["type"] == "Checkout" :
        print_total_order(selected_menu_items)
        exit()

    # The only other choice is that they selected a menu item
    # so we neeed to ask for the quantity and add that selection to 
    # the list of things they want to buy.
    else :
        user_input["quantity"] = input("Please enter the quantity: ")
        selected_menu_items.append(user_input)
