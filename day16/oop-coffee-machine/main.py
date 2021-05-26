from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    user_input = input(
        f'What would you like? {menu.get_items()}?').lower()

    if user_input == "off":
        break

    elif user_input == "report":
        coffee_maker.report()
        
    else:
        coffee = menu.find_drink(user_input)
        if coffee is not None:
            price = coffee.cost
            if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(price):
                coffee_maker.make_coffee(coffee)

 