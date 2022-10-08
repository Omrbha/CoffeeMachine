# COFFEE MAKING MACHINE
class CoffeeMaker:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.action()
    def action(self):
        self.task = input("\nWrite action (buy, fill, take, remaining, exit):")
        if self.task == "buy":
            self.buy()
            self.action()
        if self.task == "fill":
            self.fill()
            self.action()
        if self.task == "take":
            self.take()
            self.action()
        if self.task == "remaining":
            self.remaining()
            self.action()
        if self.task == "exit":
            self.exit()
    def buy(self):
        self.coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.coffee_type == "1":
            self.espresso()
        if self.coffee_type == "2":
            self.latte()
        if self.coffee_type == "3":
            self.cappuccino()
        if self.coffee_type == "back":
            self.back()
    def fill(self):
        add_water = input("Write how many ml of water you want to add:")
        self.water += int(add_water)
        add_milk = input("Write how many ml of milk you want to add:")
        self.milk += int(add_milk)
        add_beans = input("Write how many g of beans you want to add:")
        self.beans += int(add_beans)
        add_cups = input("Write how many disposable cups you want to add:")
        self.cups += int(add_cups)
    def take(self):
        money = self.money
        self.money = 0
        print(f"I gave you{money}")
    def remaining(self):
        print(f"The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.beans} g of beans")
        print(f"{self.cups} disposable cups")
        print(f"${self.money} of money")
    def exit(self):
        quit()
    def espresso(self):
        if self.water >= 250 and self.beans >= 16 or self.cups >= 1:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!")
        elif self.water < 250 or self.beans < 16 or self.cups < 1:
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough beans!")
            else:
                print("Sorry, not enough disposable cups!")
    def latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and  self.cups >= 1:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")
        elif self.water < 300 or self.milk < 75 or self.beans < 20 or self.cups < 1:
            if self.water < 300 :
                print("Sorry, not enough water!")
            elif self.milk < 75 :
                print("Sorry, not enough milk!")
            elif self.beans < 20 :
                print("Sorry, not enough beans!")
            else:
                print("Sorry, not enough disposable cups!")
    def cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and  self.cups >= 1:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
            print("I have enough resources, making you a coffee!")
        elif self.water < 200 or self.milk < 100 or self.beans < 12 or self.cups < 1:
            if self.water < 200 :
                print("Sorry, not enough water!")
            elif self.milk < 100 :
                print("Sorry, not enough milk!")
            elif self.beans < 12 :
                print("Sorry, not enough beans!")
            else:
                print("Sorry, not enough disposable cups!")
    def back(self):
        self.action()

CoffeeMaker()
    
