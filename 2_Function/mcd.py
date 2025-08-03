def calculate_tax(subtotal, tax_rate=0.08):
    """
    Calculate the tax amount based on subtotal and tax rate.
    
    Args:
        subtotal (float): The pre-tax amount
        tax_rate (float): The tax rate (default: 8%)
        
    Returns:
        float: The tax amount
    """
    pass

def format_currency(amount):
    """
    Format amount as currency with $ symbol and 2 decimal places.
    
    Args:
        amount (float): The amount to format
        
    Returns:
        str: Formatted currency string
    """
    pass

def apply_discount(subtotal, discount_percentage):
    """
    Apply a percentage discount to the subtotal.
    
    Args:
        subtotal (float): The pre-discount amount
        discount_percentage (float): Discount percentage (e.g., 10 for 10%)
        
    Returns:
        float: Discounted amount
    """
    pass

def is_meal_deal_eligible(items):
    """
    Check if the items qualify for a meal deal.
    A meal deal requires at least one main item, one side, and one drink.
    
    Args:
        items (list): List of item names
        
    Returns:
        bool: True if eligible for a meal deal, False otherwise
    """
    main_items = ["Big Mac", "Quarter Pounder", "McChicken", "Filet-O-Fish"]
    sides = ["French Fries", "Apple Slices", "Side Salad"]
    drinks = ["Coke", "Sprite", "Diet Coke", "Water", "Coffee"]
    
    pass
