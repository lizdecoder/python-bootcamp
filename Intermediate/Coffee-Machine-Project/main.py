MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def current_resources(machine_profit):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    machine_profit = '%.2f' % machine_profit
    print(f'Water: {water}mL\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${machine_profit}')


def check_resources(choice):
    # .get() gets all keys and all values associated dictionary
    # in this case the ingredient dictionary nested inside the choice dictionary
    ingredients = MENU.get(choice).get('ingredients')
    for key in ingredients:
        if resources[key] < ingredients[key]:
            # not enough water and milk for cappuccino after latte
            print(f"Sorry, there is not enough {key} for coffee.")
            return False
    return True


def check_transaction(entered_money, choice):
    drink_cost = MENU.get(choice).get('cost')
    if drink_cost > entered_money:
        return False
    elif drink_cost < entered_money:
        change = '%.2f' % (entered_money - drink_cost)
        print(f"Here is ${change} dollars in change.")
    return True


def deduct_ingredients(choice):
    ingredients = MENU.get(choice).get('ingredients')
    for key in ingredients:
        resources[key] -= ingredients[key]


resources_available = True
profit = float(0)

while resources_available:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ")
    if user_choice == 'report':
        current_resources(profit)
    elif user_choice in MENU:
        if check_resources(user_choice):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            user_money = round((quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01), 2)
            if check_transaction(user_money, user_choice):
                profit += MENU.get(user_choice).get('cost')
                deduct_ingredients(user_choice)
                print(f"Here is your ☕️ {user_choice}. Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded.")
        else:
            resources_available = False
    elif user_choice == 'off':
        resources_available = False
        print("machine turning off")
    else:
        print("invalid choice. try again.")
