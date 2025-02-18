# Ice Cream Shop Application
# Author: Thanh Nam Trinh
# Date: 1/29/2025

# Store our ice cream shop's menu items
flavors = ["vanilla", "caramel", "mint", "strawberry", "chocolate", "blueberry"]
toppings = ["sprinkles", "nuts", "cherry"]
cone_types = ["cake cone", "sugar cone", "waffle cone"]
prices = {"scoop": 2.50, "topping": 0.50, "cone": 1.00}

def display_menu():
    """Show available flavors, toppings, and cone options to the customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    
    print("\nAvailable Flavors:")
    for flavor in flavors:
        print(f"- {flavor}")

    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    print("\nAvailable Cone Types:")
    for cone in cone_types:
        print(f"- {cone}")

    # Display the prices
    print("\nPrices:")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")
    print(f"Cones: ${prices['cone']:.2f} each")

def get_flavor():
    """Gets ice cream flavor choices from the customer"""
    chosen_flavors = []

    while True:
        try:
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops.")
        except ValueError:
            print("Please enter a number.")

    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops):
        while True:
            flavor_choice = input(f"Scoop {i+1}: ").lower()
            if flavor_choice in flavors:
                chosen_flavors.append(flavor_choice)
                break
            print("Sorry, that flavor isn't available. Please choose from the menu.")

    return num_scoops, chosen_flavors

def get_toppings():
    """Gets topping choices from the customer"""
    chosen_toppings = []
    
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        if topping == 'done':
            break
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")

    return chosen_toppings

def get_cone():
    """Gets cone choice from the customer"""
    while True:
        print("\nChoose a cone type:")
        for cone in cone_types:
            print(f"- {cone.title()}")
        cone_choice = input("Enter your cone choice: ").lower()
        if cone_choice in cone_types:
            return cone_choice
        print("Sorry, that cone type isn't available. Please choose from the menu.")

def calculate_total(num_scoops, num_toppings):
    """Calculates the total cost of the order and applies a discount if applicable"""
    scoop_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["topping"]
    cone_cost = prices["cone"]

    total = scoop_cost + topping_cost + cone_cost

    # Apply discount for orders over $10
    if total > 10:
        total *= 0.90  # 10% discount
        print("\n🎉 Congratulations! You've received a 10% discount for orders over $10.")

    return total

def print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_choice):
    """Prints a receipt for the customer"""
    print("\n=== Your Ice Cream Order ===")
    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")

    print(f"\nCone Type: {cone_choice.title()}")

    if chosen_toppings:
        print("\nToppings:")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")

    # Print the total
    total = calculate_total(num_scoops, len(chosen_toppings))
    print(f"\nTotal: ${total:.2f}")

    # Save order to file
    with open("daily_order.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops, {cone_choice} - ${total:.2f}\n")

def main():
    """Runs our ice cream shop program"""
    display_menu()
    num_scoops, chosen_flavors = get_flavor()
    chosen_toppings = get_toppings()
    chosen_cone = get_cone()
    print_receipt(num_scoops, chosen_flavors, chosen_toppings, chosen_cone)

# Automatically execute the main function when the application runs
if __name__ == "__main__":
    main()
