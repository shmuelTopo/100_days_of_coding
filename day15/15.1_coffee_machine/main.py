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

money = 0


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')


def refill(ingredient_to_fill):
    global resources
    if ingredient_to_fill.lower() == "water":
        resources["water"] = 300
    elif ingredient_to_fill.lower() == "milk":
        resources["milk"] = 200
    elif ingredient_to_fill.lower() == "coffee":
        resources["coffee"] = 100
    else:
        print(f'Sorry {ingredient_to_fill} is not in our inventory!')


def enough_resources(type_of_coffee):
    there_is_enough = True
    if type_of_coffee not in MENU.keys():
        print(f'There is no {type_of_coffee} in our machine...')
        return False
    for ingredient_k, amount_v in MENU[type_of_coffee]["ingredients"].items():
        if amount_v > resources[ingredient_k]:
            print(f'Sorry there is not enough {ingredient_k}.')
            there_is_enough = False
    return there_is_enough


def collect_money():
    total = 0
    try:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))

        total += quarters * 0.25
        total += dimes * 0.10
        total += nickels * 0.05
        total += pennies * 0.01
    except ValueError:
        print("You didn't enter valid number...")
        # the function will still return whatever money the user did enter correctly
    return round(total, 2)


while True:
    user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if user_input == "report":
        report()
        continue
    if user_input == "off":
        break
    if user_input == "refill":
        ingredients = input('What would you like to refill? (separated by ,, type "all" to refill all)  ')
        if ingredients.lower() == "all":
            ingredients = "water, milk, coffee"

        ingredients = ingredients.split(', ')

        for ingredient in ingredients:
            refill(ingredient)

        continue

    if user_input == "withdraw":
        password = input("Please enter the admin password: ")
        if password == "1234":
            print(f"Here is ${money}")
            money = 0
        else:
            print("Wrong password!!")
        continue

    coffee = user_input
    if not enough_resources(coffee):
        continue

    price = MENU[coffee]["cost"]
    print(f'Please pay {price} to get you {coffee.capitalize()}...')
    money_collected = collect_money()

    print(f'You paid ${money_collected}')

    if money_collected < price:
        print("Sorry that's not enough money. Money refunded.")
        continue
    elif money_collected > price:
        print(f"Here is ${round(money_collected - price, 2)} dollars in change.")

    money += price

    for ingredient_k, amount_v in MENU[coffee]["ingredients"].items():
        resources[ingredient_k] -= amount_v
    print(f'Enjoy your {coffee}')
