from main import MENU
from main import resources

profit = 0

def make_drink(order):
    if check_resources(order):
        print(f"Making {order}...")
        return True
    return False

def check_resources(order):
    ingredients = MENU[order]["ingredients"]
    for item, required in ingredients.items():
        if required > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True

def deduct_resources(order):
    ingredients = MENU[order]["ingredients"]
    for item, required in ingredients.items():
        resources[item] -= required

def process_coins(order):
    global profit
    print("Please insert coins.")

    quarters = int(input("please put in Quarters: ")) * 0.25
    dimes = int(input("please put in Dimes: ")) * 0.10
    nickles = int(input("please put in Nickles: ")) * 0.05
    pennies = int(input("please put in Pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies

    cost = MENU[order]["cost"]
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        profit += cost
        
    print(f"Here is your {order}. Enjoy!")
    return True

# Main program loop
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        print("Turning off the machine...")
        break
    elif order == "report":
        print("Resources:")
        for item, quantity in resources.items():
            print(f"{item}: {quantity}")
        print(f"Profit: ${profit}")
    elif order in MENU:
        if make_drink(order):
            if process_coins(order):
                # Deduct ingredients from resources
                for item, amount in MENU[order]["ingredients"].items():
                    resources[item] -= amount
    else:
        print("Invalid choice.")

