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
        print("Menu # | Menu Category")
        print("------ | ---------------------------------")

        for category in menu_data.keys() : 
            x = add_whitespace(item_number, -6)
            y = add_whitespace(category.title(), 24)
            print(f"{x} | {y}")

            listed_items.append({"name": category, "price": 0, "type": "main menu choice"})
            item_number = item_number + 1


    # Print the specific menu requested by the customer
    elif menu_type.title() in menu_data :
        
        print(f"{menu_type.title()} Items:")
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
                    # a = add_whitespace(item_number, -6)
                    # b = add_whitespace(sub_item_name.title(), 20)
                    # c = add_whitespace(sub_item_price, -5)
                    # print(f"{a} |     {b} | ${c}")
                    print_menu_item(item_number, item_name+" - "+sub_item_name, sub_item_price)


                    listed_items.append({"name":sub_item_name, 
                                         "price":sub_item_price,
                                         "type":menu_type}) 

                    item_number = item_number + 1

    print()

    choice = False
    while not choice : 

        choice = input( "Select an item number, M for Main Menu, C to check out, or Q to quit: ")

        if choice.upper() == "M" : 
            pass
        elif choice.upper() == "C" : 
            pass
        elif choice.upper() == "Q" : 
            exit
        elif choice.isdigit() :
            if int(choice) < len(listed_items) and int(choice) >= 0 :
                return listed_items[int(choice)]
            else : 
                print("Error: Unknown menu selection!")
                choice = False
        else : 
            print("Error: Unknown menu selection!")
            choice = False



# MAIN PROGRAM BODY

print("\nWelcome to the Variety Food Truck!\n==================================\n")
print("The choice was: ", get_menu_input( menu, "Main" ))


# # 1. Set up order list. Order list will store a list of dictionaries for
# # menu item name, item price, and quantity ordered

# customer_order = []

# # Launch the store and present a greeting to the customer
# print()
# print("Welcome to the variety food truck.")
# print()

# # Customers may want to order multiple items, so let's create a continuous loop

# place_order = True

# while place_order:

#     # Ask the customer from which menu category they want to order
#     print("From which menu would you like to order? ")

#     # Create a variable for the menu item number
#     i = 1
    
#     # Create a dictionary to store the menu for later retrieval
#     menu_items = {}

#     # Print the options to choose from menu headings (all the first level
#     # dictionary items in menu).
#     for key in menu.keys():
#         print(f"{i}: {key}")
#         # Store the menu category associated with its menu item number
#         menu_items[i] = key
#         # Add 1 to the menu item number
#         i += 1

#     # Get the customer's input
#     menu_category = input("Type menu number: ")

#     # Check if the customer's input is a number
#     if menu_category.isdigit():
#         # Check if the customer's input is a valid option
#         if int(menu_category) in menu_items.keys():
#             # Save the menu category name to a variable
#             menu_category_name = menu_items[int(menu_category)]

#             # Print out the menu category name they selected
#             print(f"You selected {menu_category_name}")
#             print()

#             # Print out the menu options from the menu_category_name
#             print(f"What {menu_category_name} item would you like to order?")
#             i = 1
#             menu_items = {}
#             print("Item # | Item name                | Price")
#             print("-------|--------------------------|-------")

#             for key, value in menu[menu_category_name].items():
#                 # Check if the menu item is a dictionary to handle differently
#                 if type(value) is dict:
#                     for key2, value2 in value.items():
#                         num_item_spaces = 24 - len(key + key2) - 3
#                         item_spaces = " " * num_item_spaces
#                         print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
#                         menu_items[i] = {
#                             "Item name": key + " - " + key2,
#                             "Price": value2
#                         }
#                         i += 1
#                 else:
#                     num_item_spaces = 24 - len(key)
#                     item_spaces = " " * num_item_spaces
#                     print(f"{i}      | {key}{item_spaces} | ${value}")
#                     menu_items[i] = {
#                         "Item name": key,
#                         "Price": value
#                     }
#                     i += 1

#             # 2. Ask customer to input menu item number
#             menu_item = input("Please choose an item: ")

#             # 3. Check if the customer typed a number
#             if menu_item.isdigit() :

#                 # Convert the menu selection to an integer
#                 menu_item = int(menu_item)

#                 # 4. Check if the menu selection is in the menu items
#                 if menu_item in menu_items.keys()

#                     # Store the item name as a variable
#                     menu_item_name = menu_items[menu_item]

#                     # Ask the customer for the quantity of the menu item


#                     # Check if the quantity is a number, default to 1 if not


#                     # Add the item name, price, and quantity to the order list


#                     # Tell the customer that their input isn't valid


#                 # Tell the customer they didn't select a menu option

#         else:
#             # Tell the customer they didn't select a menu option
#             print(f"{menu_category} was not a menu option.")
#     else:
#         # Tell the customer they didn't select a number
#         print("You didn't select a number.")

#     while True:
#         # Ask the customer if they would like to order anything else
#         keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

#         # 5. Check the customer's input

#                 # Keep ordering

#                 # Exit the keep ordering question loop

#                 # Complete the order

#                 # Since the customer decided to stop ordering, thank them for
#                 # their order

#                 # Exit the keep ordering question loop


#                 # Tell the customer to try again


# # Print out the customer's order
# print("This is what we are preparing for you.\n")

# # Uncomment the following line to check the structure of the order
# #print(order)

# print("Item name                 | Price  | Quantity")
# print("--------------------------|--------|----------")

# # 6. Loop through the items in the customer's order

#     # 7. Store the dictionary items as variables


#     # 8. Calculate the number of spaces for formatted printing


#     # 9. Create space strings


#     # 10. Print the item name, price, and quantity


# # 11. Calculate the cost of the order using list comprehension
# # Multiply the price by quantity for each item in the order list, then sum()
# # and print the prices.
