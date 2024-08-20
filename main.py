import pygame
import sys
import Maps
import PUi
import Matcher
import Saver
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_X = 1000
SCREEN_Y = 900
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("CityLab!")

# Initialize building status
is_center_bought = False
is_paused = False
is_menu = False

# Define key mappings
KEY_FACTORY = pygame.K_1
KEY_FLAT = pygame.K_2
KEY_GAS_STATION = pygame.K_3
KEY_SHOP = pygame.K_4
KEY_GENERATOR = pygame.K_5
KEY_CENTER = pygame.K_6
KEY_WATER_TOWER = pygame.K_7

def load_image(path):
    try:
        return pygame.image.load(path).convert_alpha()
    except pygame.error as e:
        print(f"Unable to load image at {path}: {e}")
        return pygame.Surface((0, 0))  # Return a blank surface if the image fails to load

images = {
    "grass": load_image(Maps.grass),
    "sand": load_image(Maps.sand),
    "factory": load_image(Maps.factory),
    "cursor": load_image(Maps.cursor),
    "flat": load_image(Maps.Flat),
    "tree": load_image(Maps.forest),
    "GasStation": load_image(Maps.GasStation),
    "shop": load_image(Maps.shop),
    "generetor": load_image(Maps.elecricyty),
    "centre": load_image(Maps.Centre),
    "water": load_image(Maps.water)
}

# Generate unique save name based on current date and time
now = datetime.now()
date_string = now.strftime('%Y-%m-%d_%H-%M-%S')
save_name = "save_" + date_string

# Initialize cursor position
cursor_x, cursor_y = 0, 0
columns = 15
rows = 9

def draw_map():
    cell_size = Maps.CellSize
    map_data = Maps.Map
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            pos = (x * cell_size, y * cell_size)
            if cell == 1:
                screen.blit(images["grass"], pos)
            elif cell == 2:
                screen.blit(images["sand"], pos)
            else:
                pygame.draw.rect(screen, (0, 0, 0), (pos[0], pos[1], cell_size, cell_size))

def draw_buildings():
    cell_size = Maps.CellSize
    map_data = Maps.MapBuilds
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            pos = (x * cell_size, y * cell_size)
            if cell == 1:
                screen.blit(images["factory"], pos)
            elif cell == 2:
                screen.blit(images["flat"], pos)
            elif cell == 3:
                screen.blit(images["tree"], pos)
            elif cell == 4:
                screen.blit(images["GasStation"], pos)
            elif cell == 5:
                screen.blit(images["shop"], pos)
            elif cell == 6:
                screen.blit(images["generetor"], pos)
            elif cell == 7:
                screen.blit(images["centre"], pos)
            elif cell == 8:
                screen.blit(images["centre"], pos)
            elif cell == 9:
                screen.blit(images["water"], pos)

def draw_cursor():
    cell_size = Maps.CellSize
    pos = (cursor_x * cell_size, cursor_y * cell_size)
    screen.blit(images["cursor"], pos)

def draw_pause_menu():
    overlay = pygame.Surface((SCREEN_X, SCREEN_Y))
    overlay.set_alpha(150)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, 74)
    text = font.render("Paused", True, (255, 255, 255))
    screen.blit(text, (SCREEN_X // 2 - text.get_width() // 2, SCREEN_Y // 2 - text.get_height() // 2))

    resume_text = font.render("Press ESC to Resume", True, (255, 255, 255))
    screen.blit(resume_text, (SCREEN_X // 2 - resume_text.get_width() // 2, SCREEN_Y // 2 + 130))
    save_text = font.render("Press TAB to SaveGame", True, (255, 255, 255))
    screen.blit(save_text, (SCREEN_X // 2 - save_text.get_width() // 2, SCREEN_Y // 2 + 180))
    load_text = font.render("Press L to LoadGame", True, (255, 255, 255))
    screen.blit(load_text, (SCREEN_X // 2 - load_text.get_width() // 2, SCREEN_Y // 2 + 230))
    menu_text = font.render("Press M go to main menu", True, (255, 255, 255))
    screen.blit(menu_text, (SCREEN_X // 2 - menu_text.get_width() // 2, SCREEN_Y // 2 + 280))

def draw_main_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)

    title_text = font.render("CityLab", True, (255, 255, 255))
    screen.blit(title_text, (SCREEN_X // 2 - title_text.get_width() // 2, SCREEN_Y // 2 - 150))

    start_text = font.render("Press ENTER to Start", True, (255, 255, 255))
    screen.blit(start_text, (SCREEN_X // 2 - start_text.get_width() // 2, SCREEN_Y // 2))

    quit_text = font.render("Press ESC to Quit", True, (255, 255, 255))
    screen.blit(quit_text, (SCREEN_X // 2 - quit_text.get_width() // 2, SCREEN_Y // 2 + 100))

    pygame.display.update()

def handle_events():
    global is_paused, is_center_bought, cursor_x, cursor_y, is_menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_paused = not is_paused
            elif event.key == pygame.K_TAB:
                Saver.SaveGame(save_name)
                print("Game Saved")
            elif event.key == pygame.K_l:
                Saver.LoadGame(save_name)
                print(f"Game Loaded: {save_name}")
            elif event.key == pygame.K_m:
                is_menu = True
            elif event.key == pygame.K_a and cursor_x > 0:
                Maps.MapCursor[cursor_y][cursor_x] = 0
                cursor_x -= 1
                Maps.MapCursor[cursor_y][cursor_x] = 1
            elif event.key == pygame.K_d and cursor_x < columns - 1:
                Maps.MapCursor[cursor_y][cursor_x] = 0
                cursor_x += 1
                Maps.MapCursor[cursor_y][cursor_x] = 1
            elif event.key == pygame.K_w and cursor_y > 0:
                Maps.MapCursor[cursor_y][cursor_x] = 0
                cursor_y -= 1
                Maps.MapCursor[cursor_y][cursor_x] = 1
            elif event.key == pygame.K_s and cursor_y < rows - 1:
                Maps.MapCursor[cursor_y][cursor_x] = 0
                cursor_y += 1
                Maps.MapCursor[cursor_y][cursor_x] = 1
            elif event.key == KEY_FACTORY and Matcher.money >= 1000:
                Maps.MapBuilds[cursor_y][cursor_x] = 1
                Matcher.MinusMoney(1000)
                Matcher.factories += 1
                Matcher.PeoplesHapines -= 0.1
            elif event.key == KEY_FLAT and Matcher.money >= 10:
                Maps.MapBuilds[cursor_y][cursor_x] = 2
                Matcher.MinusMoney(10)
                Matcher.AddPeoples(10)
            elif event.key == KEY_GAS_STATION and Matcher.money >= 120:
                Maps.MapBuilds[cursor_y][cursor_x] = 4
                Matcher.MinusMoney(120)
                Matcher.GasStations += 1
                Matcher.product_cost += 1
            elif event.key == KEY_SHOP and Matcher.money >= 200:
                Maps.MapBuilds[cursor_y][cursor_x] = 5
                Matcher.MinusMoney(200)
                Matcher.shops += 1
                if Matcher.PeoplesHapines <= 100:
                    Matcher.PeoplesHapines += 30
            elif event.key == KEY_GENERATOR and Matcher.money >= 500:
                Maps.MapBuilds[cursor_y][cursor_x] = 6
                Matcher.MinusMoney(500)
                Matcher.Volts += 100
                Matcher.generators += 1
            elif event.key == KEY_CENTER and Matcher.money >= 10000 and not is_center_bought:
                is_center_bought = True
                Maps.MapBuilds[cursor_y][cursor_x] = 7
                Matcher.MinusMoney(10000)
            elif event.key == KEY_WATER_TOWER and Matcher.money >= 500:
                Maps.MapBuilds[cursor_y][cursor_x] = 9
                Matcher.MinusMoney(500)
                Matcher.water_towerwers += 1
            elif event.key == pygame.K_SPACE:
                if Matcher.product > 0:
                    total_sale = Matcher.product_cost * Matcher.product
                    Matcher.product_cost += Matcher.money
                    Matcher.product = 0
                    Matcher.AddMoney(total_sale)
            elif event.key == pygame.K_LCTRL:
                total_tax = Matcher.peoples * Matcher.tax
                Matcher.TotalTax += total_tax
                Matcher.AddMoney(total_tax)
                if Matcher.peoples > 0:
                    Matcher.PeoplesHapines -= 1
                print(f"shops: {Matcher.shops}, TotalShops: {Matcher.TotalShops}, PeoplesHapines: {Matcher.PeoplesHapines}")
    return True

def update_game_state():
    if Matcher.factories > 0:
        Matcher.product += 0.5 * Matcher.factories
    if Matcher.product >= 1000:
        Matcher.ecology -= 0.1
        Matcher.PeoplesHapines -= 10
    if Matcher.product > 900 and is_center_bought:
        total_sale = Matcher.product_cost * Matcher.product
        Matcher.AddMoney(total_sale)
        Matcher.product = 0

    Matcher.generate_power()
    Matcher.VoltsToHouses()
    Matcher.happiness_destroy()
    Matcher.generate_water()
    Matcher.WaterToHouses()
    Matcher.hapynes_add()

def main_loop():
    global cursor_x, cursor_y
    running = True
    while running:
        if is_paused:
            draw_pause_menu()
            pygame.display.update()
            if is_menu:
                draw_main_menu()
                pygame.display.update()
            running = handle_events()
            continue

        # Game logic
        update_game_state()

        # Handle events and update game state
        if not handle_events():
            break

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the map, buildings, and cursor
        draw_map()
        draw_buildings()
        draw_cursor()
        PUi.DrawUi(screen, (0, 600), Matcher.money, Matcher.peoples, Matcher.product, Matcher.ecology,
                   Matcher.PeoplesHapines, Matcher.Volts, Matcher.Water)
        PUi.DrawPicture(screen, (0, 600), Matcher.ecology)

        # Update the display
        pygame.display.update()

def main():
    while True:
        draw_main_menu()
        pygame.display.update()

        # Handle menu events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Start the main function
main()
