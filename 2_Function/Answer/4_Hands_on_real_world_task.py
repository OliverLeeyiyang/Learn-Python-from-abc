"""
McDonald's Ordering System

This module demonstrates how to use functions to solve a real-world problem:
creating an ordering system for a McDonald's restaurant.

Task for students:
1. Complete the display_menu() function to show all items with prices
2. Complete the take_order() function to allow customers to select items
3. Complete the calculate_total() function to determine the final price
4. Complete the generate_receipt() function to create a formatted receipt
"""

# Import helper functions from the extension file
from extension import calculate_tax, format_currency, apply_discount, is_meal_deal_eligible

# McDonald's menu with prices
MENU = {
    "Big Mac": 5.99,
    "Quarter Pounder": 6.49,
    "McChicken": 4.99,
    "Filet-O-Fish": 5.49,
    "French Fries": 2.99,
    "Apple Slices": 1.99,
    "Side Salad": 2.49,
    "Coke": 1.79,
    "Sprite": 1.79,
    "Diet Coke": 1.79,
    "Water": 1.29,
    "Coffee": 1.99
}

def display_menu():
    """
    Display the McDonald's menu with prices.
    
    Returns:
        None
    """
    print("\n===== McDonald's Menu =====")
    print("Item".ljust(20) + "Price")
    print("-" * 30)
    
    # Display each menu item with its price
    for item, price in MENU.items():
        print(f"{item.ljust(20)} {format_currency(price)}")
    
    print("=" * 30)

def take_order():
    """
    Take a customer order by allowing them to select multiple items.
    
    Returns:
        list: A list of dictionaries containing item names and quantities
    """
    order = []
    
    while True:
        item = input("Enter menu item (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item not in MENU:
            print("Item not on menu, please choose again.")
            continue
        quantity = input(f"Enter quantity for {item}: ")
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity, please enter a positive number.")
            continue
        order.append({"name": item, "quantity": quantity})
    
    return order

def calculate_total(order):
    """
    Calculate the total cost of the order including tax and applying any discounts.
    
    Args:
        order (list): List of dictionaries containing item names and quantities
        
    Returns:
        tuple: (subtotal, tax, discount, total) as floats
    """
    subtotal = 0.0
    
    # Calculate the subtotal by multiplying each item's price by its quantity
    for item in order:
        name = item["name"]
        quantity = item["quantity"]
        subtotal += MENU[name] * quantity
    
    # Check if the order qualifies for a meal deal (10% discount)
    ordered_items = [item["name"] for item in order]
    discount = 0.0
    
    # Check for meal deals and apply discount if eligible
    if is_meal_deal_eligible(ordered_items):
        discount = apply_discount(subtotal, 0.10)  # 10% discount
    
    # Calculate tax using the helper function
    tax = calculate_tax(subtotal - discount)
    
    # Calculate final total
    total = subtotal - discount + tax
    
    return (subtotal, tax, discount, total)

def generate_receipt(order, financial_details):
    """
    Generate a formatted receipt for the customer's order.
    
    Args:
        order (list): List of dictionaries containing item names and quantities
        financial_details (tuple): (subtotal, tax, discount, total)
        
    Returns:
        str: Formatted receipt text
    """
    subtotal, tax, discount, total = financial_details
    receipt = []
    
    # Receipt header
    receipt.append("===== McDonald's Receipt =====")
    receipt.append("Item".ljust(20) + "Qty".ljust(10) + "Price".rjust(10))
    receipt.append("-" * 40)
    
    # List of ordered items
    for item in order:
        name = item["name"]
        quantity = item["quantity"]
        price = MENU[name] * quantity
        receipt.append(f"{name.ljust(20)} {str(quantity).ljust(10)} {format_currency(price).rjust(10)}")
    
    receipt.append("-" * 40)
    
    # Financial summary
    receipt.append(f"{'Subtotal:':.<30} {format_currency(subtotal)}")
    if discount > 0:
        receipt.append(f"{'Discount:':.<30} -{format_currency(discount)}")
    receipt.append(f"{'Tax:':.<30} {format_currency(tax)}")
    receipt.append(f"{'Total:':.<30} {format_currency(total)}")
    receipt.append("=" * 40)
    receipt.append("Thank you for choosing McDonald's!")
    
    return "\n".join(receipt)

def main():
    """Main function to run the McDonald's ordering system."""
    print("Welcome to McDonald's!")
    
    # Display the menu
    display_menu()
    
    # Take the customer's order
    order = take_order()
    
    # Calculate totals
    financial_details = calculate_total(order)
    
    # Generate and print receipt
    receipt = generate_receipt(order, financial_details)
    print(receipt)
    
    print("Thank you for ordering at McDonald's!")

if __name__ == "__main__":
    main()

