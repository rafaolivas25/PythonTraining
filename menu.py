# Restaurant Menu
def menu():
    # building menu
    title = "Restaurant menu".upper()
    print(title.center(30, "="))
    print("Here are the options:  ")

    # Display hot drinks options
    hot_drinks()

    # Display cold drinks options
    cold_drinks()

    # Display dessert options
    dessert()

    # Display fish dishes
    fish_dishes()

    # Display meat dishes
    meat_dishes()

    print("=" * 30)

# Hot drinks options
def hot_drinks():
    title = "Hot Drinks".upper()
    print(title.center(30, "="))
    print("1. Coffee".ljust(20, ".") + "1$")
    print("2. Tea".ljust(20, ".") + "1.5$")
    print("3. Hot Chocolate".ljust(20, ".") + "2$")

# Cold drinks options
def cold_drinks():
    title = "Cold Drinks".upper()
    print(title.center(30, "="))
    print("4. Water 1L".ljust(20, ".") + "2$")
    print("5. Coke".ljust(20, ".") + "1.5$")
    print("6. Iced Tea".ljust(20, ".") + "2$")

def Beverages():
    title = "Beverages".upper()
    print(title.center(30, "="))
    print("7. Beer".ljust(20, ".") + "1.2$")
    print("8. Vodka".ljust(20, ".") + "2$")

def Wines():
    title = "Wines".upper()
    print(title.center(30, "="))
    print("9. Red Wine".ljust(20, ".") + "1.2$")
    print("10. White Wine".ljust(20, ".") + "2$")

# Dessert options
def dessert():
    title = "Dessert".upper()
    print(title.center(30, "="))
    print("11. Ice cream".ljust(20, ".") + "1.5$")
    print("12. Cheese Cake".ljust(20, ".") + "3$")

# Fish dishes
def fish_dishes():
    title = "Fish Dishes".upper()
    print(title.center(30, "="))
    print("13. Grilled Salmon".ljust(20, ".") + "12$")
    print("14. Fish Tacos".ljust(20, ".") + "10$")
    print("15. Shrimp Pasta".ljust(20, ".") + "14$")

# Meat dishes
def meat_dishes():
    title = "Meat Dishes".upper()
    print(title.center(30, "="))
    print("16. Steak".ljust(20, ".") + "15$")
    print("17. Chicken Parmesan".ljust(20, ".") + "13$")
    print("18. Beef Burger".ljust(20, ".") + "11$")
    print("19. Pork Chops".ljust(20, ".") + "15$")

def side_dishes():
    title = "Side Dishes".upper()
    print(title.center(30, "="))
    print("20. Rice".ljust(20, ".") + "1$")
    print("21. Fries".ljust(20, ".") + "1$")
    print("21. Salad".ljust(20, ".") + "1$")
    print("23 Sweet Potato. ".ljust(20, ".") + "1$")

# Customer choices
def get_choice():
    choices = []
    while True:
        choice = input("Enter the number of your choice (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        elif choice.isdigit() and 1 <= int(choice) <= 23:
            choices.append(int(choice))
        else:
            print("Invalid choice. Please enter a number from 1 to 23, or 'done' to finish.")
    return choices

# Map choices to menu items and prices
def map_choices_to_items(choices):
    menu_items = {
        1: ("Coffee", 1),
        2: ("Tea", 1.5),
        3: ("Hot Chocolate", 2),
        4: ("Water 1L", 2),
        5: ("Coke", 1.5),
        6: ("Iced Tea", 2),
        7: ("Ice cream", 1.5),
        8: ("Cheese Cake", 3),
        9: ("Grilled Salmon", 12),
        10: ("Fish Tacos", 10),
        11: ("Shrimp Pasta", 14),
        12: ("Steak", 15),
        13: ("Chicken Parmesan", 13),
        14: ("Beef Burger", 11),
        15: ("Pork Chops", 15)
    }
    return [(menu_items[choice][0], menu_items[choice][1]) for choice in choices]

# Display final choices and calculate total price
def display_choices(name, choices):
    total_price = 0
    print(f"\n{name}'s choices:")
    for item, price in choices:
        print(f"- {item}: ${price}")
        total_price += price
    print(f"Total Price for {name}: ${total_price}")

# Function to take orders for each person
def take_order(name):
    all_choices = []
    while True:
        print(f"\n{name}, please choose your items:")
        menu()
        choices = get_choice()
        mapped_choices = map_choices_to_items(choices)
        all_choices.extend(mapped_choices)
        
        more = input(f"{name}, do you want to add more items? (yes/no): ")
        if more.lower() != 'yes':
            break
    return all_choices


def main():
    num_people = int(input("How many people are there? "))
    orders = []

    for i in range(num_people):
        name = input(f"Enter the name of person {i+1}: ")
        choices = take_order(name)
        orders.append((name, choices))

    for name, choices in orders:
        display_choices(name, choices)


main()
