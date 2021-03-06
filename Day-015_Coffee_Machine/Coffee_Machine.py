from menu import MENU


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: R${money}')


def check_resources(request):
    for ingredient in request:
        if request[ingredient] >= resources[ingredient]:
            return False
    return True


def insert_coin():
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01


def check_money(cost):
    return money < cost


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00

while True:
    flavour = input("What would you like? (espresso/latte/cappuccino):").lower()
    if flavour in [item for item in MENU]:
        print(f"Você selecionou {flavour}, seu custo é de R${MENU[flavour]['cost']}")
        if not check_resources(MENU[flavour]['ingredients']):
            print('Sorry, not enough resources.')
            continue
        while check_money(MENU[flavour]['cost']):
            money += insert_coin()
            money = round(money, 2)
            print(f'Total inserido: R${money}')
            if check_money(MENU[flavour]['cost']):
                if input('Dinheiro insuficiente, deseja inserir mais moedas? "s" ou "n"').lower() == 'n':
                    print(f'Retire seu dinheiro: R${money}')
                    money = 0.0
                    break
        for ingredient in MENU[flavour]['ingredients']:
            resources[ingredient] -= MENU[flavour]['ingredients'][ingredient]
        money -= MENU[flavour]['cost']
        print('Retire seu pedido')
        if money > 0:
            if input('Deseja continuar comprando? "s" ou "n". ') == 'n':
                print(f"Retire seu troco de R${money}")
                money = 0.0
            else:
                continue
    elif flavour == 'report':
        report()
        continue
    else:
        print("Invalid flavour")
        continue

