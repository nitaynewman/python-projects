MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "cafe_api": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "cafe_api": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "cafe_api": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "cafe_api": 100,
}


def sufficient_resources(order_ingridient):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingridient:
        if order_ingridient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def coins():
    print("please insert your coins:")
    total = int(input("how meny quarters? ")) * 0.25
    total += int(input("how meny dimes? ")) * 0.1
    total += int(input("how meny nickles? ")) * 0.05
    total += int(input("how meny pennies? ")) * 0.01
    return total


def enough_money(Money, cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if Money >= cost:
        change = round(Money - cost, 2)
        print(f"here's your change ${change}")
        global profit
        profit += cost
        return True
    else:
        print("oops there isn't enough money to by that drink try again")
        return False


def coffe_maker(order, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order} ☕️. Enjoy!")


profit = 0
is_on = True
while is_on:
    Money = 0
    opttions = input("What would you like? (espresso/latte/cappuccino): ")
    if opttions == "off":
        print("see u next coffe break")
        is_on = False
    elif opttions == "report":
        print(
            f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['cafe_api']}g \nMoney: ${Money}")
    else:
        drink = MENU[opttions]
        if sufficient_resources(drink['ingredients']):
            Money = coins()
            if enough_money(Money, drink['cost']):
                coffe_maker(opttions, drink['ingredients'])
