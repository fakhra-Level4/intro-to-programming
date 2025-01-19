# Vending machine items and prices
import os
import time

# Vending machine items and prices
vending_machine = {
    "1": {"name": "Milk Chocolate", "price": 1.75, "stock": 10, "category": "Chocolates"},
    "2": {"name": "White Bread", "price": 1.80, "stock": 8, "category": "Bread"},
    "3": {"name": "Lollipops", "price": 0.50, "stock": 12, "category": "Candies"},
    "4": {"name": "Iced Tea", "price": 1.60, "stock": 8, "category": "Cold Drinks"},
    "5": {"name": "Soda", "price": 1.50, "stock": 10, "category": "Cold Drinks"},
    "6": {"name": "Chocolate Bar", "price": 1.50, "stock": 8, "category": "Chocolates"},
    "7": {"name": "Candy Bar", "price": 0.75, "stock": 10, "category": "Candies"},
    "8": {"name": "Gummy Bears", "price": 1.00, "stock": 6, "category": "Candies"},
    "9": {"name": "Pretzels", "price": 1.25, "stock": 3, "category": "Chips"},
    "10": {"name": "Corn Chips", "price": 1.20, "stock": 4, "category": "Chips"},
    "11": {"name": "Multigrain Bread", "price": 2.80, "stock": 5, "category": "Bread"},
    "12": {"name": "Latte", "price": 3.00, "stock": 4, "category": "Hot Drinks"},
    "13": {"name": "Cheese Puffs", "price": 1.00, "stock": 8, "category": "Chips"},
    "14": {"name": "Dark Chocolate", "price": 2.00, "stock": 5, "category": "Chocolates"},
    "15": {"name": "Baguette", "price": 2.20, "stock": 4, "category": "Bread"},
    "16": {"name": "Lemonade", "price": 1.40, "stock": 5, "category": "Cold Drinks"},
    "17": {"name": "Sourdough Bread", "price": 3.00, "stock": 6, "category": "Bread"},
    "18": {"name": "Candy Canes", "price": 1.50, "stock": 4, "category": "Candies"},
    "19": {"name": "Water", "price": 1.25, "stock": 12, "category": "Cold Drinks"},
    "20": {"name": "Juice", "price": 1.80, "stock": 4, "category": "Cold Drinks"},
    "21": {"name": "Chocolate Mint", "price": 1.80, "stock": 3, "category": "Chocolates"},
    "22": {"name": "Whole Wheat Bread", "price": 2.50, "stock": 10, "category": "Bread"},
    "23": {"name": "White Chocolate", "price": 2.25, "stock": 4, "category": "Chocolates"},
    "24": {"name": "Hot Chocolate", "price": 2.20, "stock": 1, "category": "Hot Drinks"},
    "25": {"name": "Tea", "price": 1.75, "stock": 5, "category": "Hot Drinks"},
    "26": {"name": "Chai Latte", "price": 2.50, "stock": 6, "category": "Hot Drinks"},
    "27": {"name": "Chocolate Croissant", "price": 2.80, "stock": 4, "category": "Bread"},
    "28": {"name": "Caramel Popcorn", "price": 1.30, "stock": 8, "category": "Snacks"},
    "29": {"name": "Spicy Nachos", "price": 1.60, "stock": 5, "category": "Chips"},
    "30": {"name": "Apple Juice", "price": 2.00, "stock": 7, "category": "Cold Drinks"}
}

#Show the categories to choose from
def display_menu():
    print("Category No.\tCategory\n")
    print("1\t\tAll items")
    print("2\t\tCold Drinks")
    print("3\t\tHot Drinks")
    print("4\t\tBread")
    print("5\t\tChips")
    print("6\t\tChocolates")
    print("7\t\tCandies")

def show_items_in_category(category_input):
    print("\t  Product\t       Price\t\tStock")
    for item_no, item in vending_machine.items():
        if item['stock'] > 0:
            # If "All items" is selected, display all items
            if category_input == "All items" or item['category'].lower() == category_input.lower():
                print(f"Item {item_no:<3}: {item['name']:<20} ${item['price']:<15} {item['stock']:<5}")

def ask_for_bread(category_input):
    want_bread = input("\nWould you like to add some bread with your hot drink? (yes/no): ").lower()
    if want_bread == 'yes':
        show_items_in_category("Bread")
        while True:
            os.system("cls")
            show_items_in_category("Bread")
            item_code = input("\nEnter the code of the bread you want to add to your order (or type 'no' to skip): ")

            if item_code.lower() == 'no':
                break
            elif item_code not in vending_machine or (category_input != "All items" and vending_machine[item_code]['category'].lower() != "bread") or vending_machine[item_code]['stock'] == 0:
                print("\nInvalid code or item is out of stock. Please try again.")
                time.sleep(1)
                os.system("cls")
                continue
            else:
                selected_item = vending_machine[item_code]
                while True:
                    try:
                        os.system("cls")
                        show_items_in_category("bread")
                        user_money = float(input(f"\nPlease insert money for {selected_item['name']} (${selected_item['price']}): $"))
                    except ValueError:
                        print("\nInvalid input. Please enter a valid amount of money.")
                        time.sleep(1)
                        os.system("cls")
                        continue

                    if user_money >= selected_item['price']:
                        change = user_money - selected_item['price']
                        print(f"\nDispensing {selected_item['name']}...")
                        print(f"\nYour change is ${change:.2f}.")
                        vending_machine[item_code]['stock'] -= 1
                        category_input = "Bread"
                        break
                break
    elif want_bread == 'no':
        pass
    else:
        print("\nInvalid input. Please respond with 'yes' or 'no'.")

def vending_machine_run():
    while True:
        # Show the category menu and ask user to select a category
        display_menu()
        category_no = input("\nEnter the number of the category you want to browse (or type 'exit' to quit): ")

        if category_no == "1":
            category_input = "All items"
        elif category_no == "2":
            category_input = "Cold Drinks"
        elif category_no == "3":
            category_input = "Hot Drinks"
        elif category_no == "4":
            category_input = "Bread"
        elif category_no == "5":
            category_input = "Chips"
        elif category_no == "6":
            category_input = "Chocolates"
        elif category_no == "7":
            category_input = "Candies"
        elif category_no.lower() == "exit":
            print("\nThank you for using the Vending Machine! Goodbye!")
            break
        else:
            print("\nInvalid input. Please try again.")
            time.sleep(1)
            os.system("cls")
            continue
        
        while True:
            os.system("cls")

            show_items_in_category(category_input)

            item_code = input("\nEnter the code of the item you want to buy (or type 'exit' to quit): ")

            if item_code.lower() == 'exit':
                break

            # Check if the item code exists and belongs to the selected category
            if item_code not in vending_machine or (category_input != "All items" and vending_machine[item_code]['category'].lower() != category_input.lower()) or vending_machine[item_code]['stock'] == 0:
                print("\nInvalid code or item is out of stock. Please try again.")
                time.sleep(1)
                os.system("cls")
                continue

            #Store the selected item's information for use later
            selected_item = vending_machine[item_code]

            # Ask for money input
            while True:
                try:
                    os.system("cls")
                    show_items_in_category(category_input)
                    user_money = float(input(f"\nPlease insert money for {selected_item['name']} (${selected_item['price']}): $"))
                except ValueError:
                    print("\nInvalid input. Please enter a valid amount of money.")
                    time.sleep(1)
                    os.system("cls")
                    continue

                if user_money >= selected_item['price']:
                    change = user_money - selected_item['price']
                    print(f"\nDispensing {selected_item['name']}...")
                    print(f"\nYour change is ${change:.2f}.")
                    #Deduct one from stock
                    vending_machine[item_code]['stock'] -= 1

                    #Ask if customer wants bread with the hot drink
                    if selected_item['category'] == "Hot Drinks":
                        while True:
                            ask_for_bread(category_input)
                            category_input = "Bread"
                            break
                    break
                
                else:
                    print("\nInsufficient funds. Please insert more money.")
                    time.sleep(1)
                    os.system("cls")
                    continue
            
            while True:
                buy_more = input("\nWould you like to buy another item from this category? (yes/no): ").lower()
                if buy_more == 'yes':
                    os.system("cls")
                    break  # Stay in the same category and continue shopping
                elif buy_more == "no":
                    print("\nThank you for using the Vending Machine! Goodbye!")
                    time.sleep(1)
                    os.system("cls")
                    break  # Exit the item-buying loop and go back to category selection
                else:
                    print("\nInvalid input.")
                    time.sleep(1)
                    #os.system("cls")
                    continue

            if buy_more == "no":
                break
        os.system("cls")

# Run the vending machine
if __name__ == "__main__":
    os.system("cls")
    vending_machine_run()