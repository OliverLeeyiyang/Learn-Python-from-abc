class Food:
    """Class representing a food item with possible modifications"""
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.possible_modifications = {}  # name: price_adjustment
        self.selected_modifications = []
    
    def add_possible_modification(self, mod_name, price_adjustment=0.0):
        """Add a possible modification for this food item"""
        self.possible_modifications[mod_name] = price_adjustment
    
    def add_multiple_modifications(self, mods_dict):
        """Add multiple possible modifications at once"""
        self.possible_modifications.update(mods_dict)
    
    def select_modification(self, mod_name):
        """Select a modification for this food item"""
        if mod_name in self.possible_modifications:
            self.selected_modifications.append(mod_name)
            return True
        return False
    
    def remove_modification(self, mod_name):
        """Remove a selected modification"""
        if mod_name in self.selected_modifications:
            self.selected_modifications.remove(mod_name)
            return True
        return False
    
    def calculate_price(self):
        """Calculate the total price with all selected modifications"""
        total = self.base_price
        for mod in self.selected_modifications:
            total += self.possible_modifications.get(mod, 0)
        return total
    
    def get_description(self):
        """Get a description of the food with selected modifications"""
        if not self.selected_modifications:
            return f"{self.name} (${self.base_price:.2f})"
        
        mods_text = ", ".join(self.selected_modifications)
        return f"{self.name} with {mods_text} (${self.calculate_price():.2f})"
    
    def display_options(self):
        """Display all available modifications"""
        print(f"\nAvailable modifications for {self.name}:")
        for mod, price in self.possible_modifications.items():
            price_text = f"+${price:.2f}" if price > 0 else f"-${abs(price):.2f}" if price < 0 else "no charge"
            print(f"  • {mod}: {price_text}")


class Category:
    """Class representing a food category containing multiple food items"""
    def __init__(self, name):
        self.name = name
        self.foods = {}  # name: Food object
    
    def add_food(self, food):
        """Add a Food object to this category"""
        if isinstance(food, Food):
            self.foods[food.name] = food
            return True
        return False
    
    def remove_food(self, food_name):
        """Remove a food item from this category"""
        if food_name in self.foods:
            del self.foods[food_name]
            return True
        return False
    
    def get_food(self, food_name):
        """Get a specific food item by name"""
        return self.foods.get(food_name)
    
    def display_foods(self):
        """Display all foods in this category"""
        print(f"\n=== {self.name} ===")
        for name, food in self.foods.items():
            print(f"  {name}: ${food.base_price:.2f}")
    
    def get_all_food_names(self):
        """Return a list of all food names in this category"""
        return list(self.foods.keys())


class Menu:
    """Class representing the complete menu containing multiple categories"""
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.categories = {}  # name: Category object
        self.current_order = []  # List of (Food, selected_mods) tuples
    
    def add_category(self, category):
        """Add a Category object to the menu"""
        if isinstance(category, Category):
            self.categories[category.name] = category
            return True
        return False
    
    def remove_category(self, category_name):
        """Remove a category from the menu"""
        if category_name in self.categories:
            del self.categories[category_name]
            return True
        return False
    
    def display_categories(self):
        """Display all categories in the menu"""
        print(f"\n=== {self.restaurant_name} Menu Categories ===")
        for name in self.categories:
            print(f"• {name}")
    
    def display_category(self, category_name):
        """Display all foods in a specific category"""
        if category_name in self.categories:
            self.categories[category_name].display_foods()
        else:
            print(f"Category '{category_name}' not found!")
    
    def search_food(self, food_name):
        """Search for a food item across all categories"""
        found_items = []
        
        for category_name, category in self.categories.items():
            food = category.get_food(food_name)
            if food:
                found_items.append((category_name, food))
        
        if found_items:
            print(f"\nFound '{food_name}' in:")
            for category_name, food in found_items:
                print(f"  {category_name}: ${food.base_price:.2f}")
            return found_items
        else:
            print(f"'{food_name}' not found in any category")
            return []
    
    def get_food(self, food_name):
        """Get a food item by name from any category"""
        for category in self.categories.values():
            food = category.get_food(food_name)
            if food:
                return food
        return None
    
    def display_full_menu(self):
        """Display the complete menu with all categories and foods"""
        print(f"\n=== {self.restaurant_name} Complete Menu ===")
        for category_name, category in self.categories.items():
            print(f"\n{category_name}:")
            for food_name, food in category.foods.items():
                print(f"  {food_name}: ${food.base_price:.2f}")
    
    def add_to_order(self, food_name):
        """Add a food item to the current order"""
        food = self.get_food(food_name)
        if food:
            # Create a copy of the food item for this order
            # This allows the same food to be ordered multiple times with different modifications
            import copy
            food_copy = copy.deepcopy(food)
            self.current_order.append(food_copy)
            print(f"Added '{food_name}' to your order")
            return food_copy
        else:
            print(f"'{food_name}' not found in menu")
            return None
    
    def remove_from_order(self, index):
        """Remove a food item from the current order by index"""
        if 0 <= index < len(self.current_order):
            removed = self.current_order.pop(index)
            print(f"Removed '{removed.name}' from your order")
            return True
        else:
            print(f"Invalid order index: {index}")
            return False
    
    def calculate_order_total(self):
        """Calculate the total price of the current order"""
        total = 0
        
        print("\n=== Order Summary ===")
        for i, food in enumerate(self.current_order):
            price = food.calculate_price()
            total += price
            print(f"{i+1}. {food.get_description()}")
        
        print(f"\nTotal: ${total:.2f}")
        return total
    
    def clear_order(self):
        """Clear the current order"""
        self.current_order = []
        print("Order cleared")
    

# Helper function to create a sample McDonald's menu
def create_mcdonalds_menu():
    # Create the main menu
    mcdonalds = Menu("McDonald's")
    
    # Create categories
    burgers = Category("Burgers")
    chicken = Category("Chicken")
    breakfast = Category("Breakfast")
    sides = Category("Sides")
    beverages = Category("Beverages")
    desserts = Category("Desserts")
    
    # Add categories to menu
    for category in [burgers, chicken, breakfast, sides, beverages, desserts]:
        mcdonalds.add_category(category)
    
    # Create and add burger items
    big_mac = Food("Big Mac", 5.99)
    big_mac.add_multiple_modifications({
        "Extra Patty": 1.50,
        "No Pickles": 0.00,
        "Extra Cheese": 0.50,
        "No Onions": 0.00,
        "Extra Sauce": 0.25
    })
    burgers.add_food(big_mac)
    
    quarter_pounder = Food("Quarter Pounder", 6.49)
    quarter_pounder.add_multiple_modifications({
        "Extra Cheese": 0.50,
        "No Pickles": 0.00,
        "Bacon": 1.00,
        "No Onions": 0.00
    })
    burgers.add_food(quarter_pounder)
    
    cheeseburger = Food("Cheeseburger", 2.99)
    cheeseburger.add_multiple_modifications({
        "No Cheese": -0.50,
        "Extra Patty": 1.50,
        "No Pickles": 0.00
    })
    burgers.add_food(cheeseburger)
    
    # Add more burgers
    for name, price in [("Hamburger", 2.49), ("McDouble", 3.99), 
                       ("Double Quarter Pounder", 7.99), ("Filet-O-Fish", 4.99)]:
        burger = Food(name, price)
        burger.add_multiple_modifications({
            "Extra Cheese": 0.50,
            "No Pickles": 0.00,
            "No Onions": 0.00
        })
        burgers.add_food(burger)
    
    # Create and add chicken items
    nuggets_10pc = Food("McNuggets 10pc", 6.99)
    nuggets_10pc.add_multiple_modifications({
        "Extra Sauce": 0.25,
        "BBQ Sauce": 0.00,
        "Sweet & Sour Sauce": 0.00,
        "Ranch Sauce": 0.00,
        "Honey Mustard": 0.00
    })
    chicken.add_food(nuggets_10pc)
    
    nuggets_20pc = Food("McNuggets 20pc", 11.99)
    nuggets_20pc.add_multiple_modifications({
        "Extra Sauce": 0.25,
        "BBQ Sauce": 0.00,
        "Sweet & Sour Sauce": 0.00,
        "Ranch Sauce": 0.00,
        "Honey Mustard": 0.00
    })
    chicken.add_food(nuggets_20pc)
    
    # Add more chicken items
    for name, price in [("McChicken", 3.99), ("Crispy Chicken Sandwich", 5.49),
                       ("Spicy Crispy Chicken Sandwich", 5.79)]:
        item = Food(name, price)
        item.add_multiple_modifications({
            "Extra Mayo": 0.25,
            "No Lettuce": 0.00,
            "Extra Sauce": 0.25,
            "Bacon": 1.00
        })
        chicken.add_food(item)
    
    # Create and add breakfast items
    for name, price in [("Egg McMuffin", 4.49), ("Sausage McMuffin", 3.99),
                       ("Hotcakes", 4.99), ("Hash Browns", 2.49), 
                       ("Bacon, Egg & Cheese Biscuit", 4.79)]:
        item = Food(name, price)
        item.add_multiple_modifications({
            "Extra Egg": 1.00,
            "No Cheese": -0.50,
            "Extra Bacon": 1.00,
            "Extra Butter": 0.00,
            "Extra Syrup": 0.25
        })
        breakfast.add_food(item)
    
    # Create and add sides
    for name, price in [("French Fries Small", 2.99), ("French Fries Medium", 3.49),
                       ("French Fries Large", 3.99), ("Apple Slices", 1.99),
                       ("Side Salad", 2.99)]:
        item = Food(name, price)
        if "Fries" in name:
            item.add_multiple_modifications({
                "Extra Salt": 0.00,
                "No Salt": 0.00,
                "Add Cheese": 0.75
            })
        elif "Salad" in name:
            item.add_multiple_modifications({
                "Extra Dressing": 0.25,
                "No Dressing": 0.00,
                "Grilled Chicken": 1.50
            })
        sides.add_food(item)
    
    # Create and add beverages
    for name, price in [("Coca-Cola Small", 1.99), ("Coca-Cola Medium", 2.49),
                       ("Coca-Cola Large", 2.99), ("Coffee", 1.99),
                       ("Orange Juice", 2.49)]:
        item = Food(name, price)
        if "Coca-Cola" in name:
            item.add_multiple_modifications({
                "No Ice": 0.00,
                "Extra Ice": 0.00,
                "Diet Coke": 0.00,
                "Sprite": 0.00
            })
        elif "Coffee" in name:
            item.add_multiple_modifications({
                "Sugar": 0.00,
                "Cream": 0.00,
                "Extra Shot": 0.75
            })
        beverages.add_food(item)
    
    # Create and add desserts
    for name, price in [("Apple Pie", 1.99), ("McFlurry Oreo", 3.99),
                       ("Vanilla Cone", 1.49), ("Chocolate Chip Cookie", 1.99)]:
        item = Food(name, price)
        if "McFlurry" in name:
            item.add_multiple_modifications({
                "Extra Oreos": 0.50,
                "M&M's Instead": 0.00,
                "Extra Caramel": 0.25
            })
        desserts.add_food(item)
    
    return mcdonalds


# Example usage
if __name__ == "__main__":
    # Create a sample McDonald's menu
    mcdonalds_menu = create_mcdonalds_menu()
    
    # Display all categories
    mcdonalds_menu.display_categories()
    
    # Display foods in a specific category
    mcdonalds_menu.display_category("Burgers")
    
    # Search for a food item
    mcdonalds_menu.search_food("Big Mac")
    
    # Add items to order
    big_mac = mcdonalds_menu.add_to_order("Big Mac")
    if big_mac:
        big_mac.display_options()
        big_mac.select_modification("Extra Cheese")
        big_mac.select_modification("Extra Sauce")
    
    fries = mcdonalds_menu.add_to_order("French Fries Medium")
    if fries:
        fries.display_options()
        fries.select_modification("Add Cheese")
    
    mcdonalds_menu.add_to_order("Coca-Cola Medium")
    
    # Calculate order total
    mcdonalds_menu.calculate_order_total()
