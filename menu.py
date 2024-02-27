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
    
    preceeding = False 
    input_string = str(input_string)

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


def get_menu_input( menu_data, menu_type ) :
    
    item_number = 0
    listed_items = []

    # The main menu will be a little different in appearance 
    if menu_type.title() == "Main" :
        print(f"\nMenu # | Menu Category")
        print("------ | ---------------------------------")

        for category in menu_data.keys() : 
            x = add_whitespace(item_number, -6)
            y = add_whitespace(category.title(), 24)
            print(f"{x} | {y}")

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
                choice = False

        else : 
            print("Error: Unknown menu selection!")
            choice = False

def print_total_order(order) :

    total_price = 0

    print()
    print("-= Your Final Order =-")
    print()
    print(" Qty | Item                           | Price    ")
    print("---- | ------------------------------ | -------- ")

    for item in order :
        x = add_whitespace(item["quantity"], -4)
        y = add_whitespace(str(item["name"]).title(), 30)
        z = add_whitespace(item["price"], -7)
        print(f"{x} | {y} | ${z}")

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

selection = "Main"
selected_menu_items = []

while True : 

    user_input = get_menu_input( menu, selection )
    print(user_input)

    if user_input["type"] == "Main" :
        selection = "Main"

    elif user_input["type"] == "main menu choice" :
        selection = user_input["name"]

    elif user_input["type"] == "Exit" :
        print("User selected exit")
        exit()

    elif user_input["type"] == "Checkout" :
        print_total_order(selected_menu_items)
        exit()

    else :
        user_input["quantity"] = input("Please enter the quantity: ")
        selected_menu_items.append(user_input)
