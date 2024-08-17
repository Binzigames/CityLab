# stats
money = 100
peoples = 0
ecology = 100
product = 0
seals = 0


product_cost = 10

factories = 0

#match things
def AddMoney(MoneyToAdd):
    global money
    money += MoneyToAdd
    print(f"+ money {MoneyToAdd}")

def MinusMoney(MoneyToMinus):
    global money
    money -= MoneyToMinus
    print(f"- money {MoneyToMinus}")

def AddPeoples(PeoplesToAdd):
        global peoples
        peoples += PeoplesToAdd
        print(f"+ peoples {PeoplesToAdd}")

def MinusPeoples(PeoplesToMinus):
        global peoples
        peoples -= PeoplesToMinus
        print(f"- peoples {PeoplesToMinus}")


