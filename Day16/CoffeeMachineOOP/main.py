from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create an object named menu
menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()
available_items = menu.get_items() # getting the available items

while True:
    user_input = input(f"What do you want ({available_items}) : ")
    # Serving the customer
    if user_input == "off":
        print("GoodBye👋")
        break

    elif user_input == "report":
        coffee.report()
        money.report()
        continue

    drink = menu.find_drink(user_input)
    if not drink:
        continue

    if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
        coffee.make_coffee(drink)







