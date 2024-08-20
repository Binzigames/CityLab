import Matcher
import Maps


def SaveGame(Name):
    matcher_data = (
        f"{Matcher.money}\n"
        f"{Matcher.peoples}\n"
        f"{Matcher.ecology}\n"
        f"{Matcher.product}\n"
        f"{Matcher.seals}\n"
        f"{Matcher.tax}\n"
        f"{Matcher.PeoplesHapines}\n"
        f"{Matcher.Volts}\n"
        f"{Matcher.Water}\n"
        f"{Matcher.TotalTax}\n"
        f"{Matcher.product_cost}\n"
        f"{Matcher.TotalShops}\n"
        f"{Matcher.VoltsToHouse}\n"
        f"{Matcher.factories}\n"
        f"{Matcher.GasStations}\n"
        f"{Matcher.shops}\n"
        f"{Matcher.generators}\n"
        f"{Matcher.water_towerwers}\n"
    )

    map_data = "\n".join(" ".join(map(str, row)) for row in Maps.Map)
    map_builds_data = "\n".join(" ".join(map(str, row)) for row in Maps.MapBuilds)
    map_cursor_data = "\n".join(" ".join(map(str, row)) for row in Maps.MapCursor)

    with open(Name + '.txt', 'w') as file:
        file.write(matcher_data)
        file.write("\n")
        file.write(map_data)
        file.write("\n")
        file.write(map_builds_data)
        file.write("\n")
        file.write(map_cursor_data)


def LoadGame(Name):
    with open(Name + '.txt', 'r') as file:
        lines = file.readlines()

    Matcher.money = float(lines[0].strip())
    Matcher.peoples = float(lines[1].strip())
    Matcher.ecology = float(lines[2].strip())
    Matcher.product = float(lines[3].strip())
    Matcher.seals = float(lines[4].strip())
    Matcher.tax = float(lines[5].strip())
    Matcher.PeoplesHapines = float(lines[6].strip())
    Matcher.Volts = float(lines[7].strip())
    Matcher.Water = float(lines[8].strip())
    Matcher.TotalTax = float(lines[9].strip())
    Matcher.product_cost = float(lines[10].strip())
    Matcher.TotalShops = float(lines[11].strip())
    Matcher.VoltsToHouse = float(lines[12].strip())
    Matcher.factories = float(lines[13].strip())
    Matcher.GasStations = float(lines[14].strip())
    Matcher.shops = float(lines[15].strip())
    Matcher.generators = float(lines[16].strip())
    Matcher.water_towerwers = float(lines[17].strip())

    map_data = [list(map(int, line.split())) for line in lines[18:18 + Maps.rows]]
    map_builds_data = [list(map(int, line.split())) for line in lines[18 + Maps.rows:18 + 2 * Maps.rows]]
    map_cursor_data = [list(map(int, line.split())) for line in lines[18 + 2 * Maps.rows:]]

    Maps.Map = map_data
    Maps.MapBuilds = map_builds_data
    Maps.MapCursor = map_cursor_data
