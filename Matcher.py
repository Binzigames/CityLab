
# stats
money = 1000
peoples = 0
ecology = 100
product = 0
seals = 0
tax = 10
PeoplesHapines = 100
Volts = 100
Water = 100

TotalTax = 0
product_cost = 10
TotalShops = 2
VoltsToHouse = 1

factories = 0
GasStations = 0
shops = 0
generators = 0
water_towerwers = 0

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

def generate_power():
    global Volts, generators
    if generators > 0:
        power_generated = 100 * generators
        Volts += power_generated

def VoltsToHouses():
    global Volts,peoples , PeoplesHapines
    if peoples > 0 :
        NeedToPayVolts = peoples * 0.5
        Volts -= NeedToPayVolts
    if Volts < 0 :
        PeoplesHapines -= 0.1

def happiness_destroy():
    global PeoplesHapines, peoples
    if PeoplesHapines < 0:
        peoples -= 1

def generate_water():
    global Water, water_towerwers
    if water_towerwers > 0:
        water_generated = 100 * water_towerwers
        Water += water_generated

def WaterToHouses():
    global Water,peoples , PeoplesHapines
    if peoples > 0 :
        NeedToPayWater = peoples * 0.5
        Water -= NeedToPayWater
    if Water < 0 :
        PeoplesHapines -= 0.1










