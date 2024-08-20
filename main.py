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
IsCentreBought = False
IsPaused = False

# Load images
images = {
    "grass": pygame.image.load(Maps.grass).convert_alpha(),
    "sand": pygame.image.load(Maps.sand).convert_alpha(),
    "factory": pygame.image.load(Maps.factory).convert_alpha(),
    "cursor": pygame.image.load(Maps.cursor).convert_alpha(),
    "flat": pygame.image.load(Maps.Flat).convert_alpha(),
    "tree": pygame.image.load(Maps.forest).convert_alpha(),
    "GasStation": pygame.image.load(Maps.GasStation).convert_alpha(),
    "shop": pygame.image.load(Maps.shop).convert_alpha(),
    "generetor": pygame.image.load(Maps.elecricyty).convert_alpha(),
    "centre": pygame.image.load(Maps.Centre).convert_alpha(),
    "water": pygame.image.load(Maps.water).convert_alpha()
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

# Main loop
running = True
while running:
    if IsPaused:
        draw_pause_menu()
        pygame.display.update()

        # Handle events while paused
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    IsPaused = False
                elif event.key == pygame.K_TAB:
                    Saver.SaveGame(save_name)
                    print("game Saved")
                elif event.key == pygame.K_l:
                    Saver.LoadGame(save_name)
                    print("game loaded  :" + save_name)
        continue

    # Game logic
    if Matcher.factories > 0:
        Matcher.product += 0.5 * Matcher.factories
    if Matcher.product >= 1000:
        Matcher.ecology -= 0.1
        Matcher.PeoplesHapines -= 10
    if Matcher.product > 900 and IsCentreBought:
        total_sale = Matcher.product_cost * Matcher.product
        Matcher.AddMoney(total_sale)
        Matcher.product = 0

    Matcher.generate_power()
    Matcher.VoltsToHouses()
    Matcher.happiness_destroy()
    Matcher.generate_water()
    Matcher.WaterToHouses()
    Matcher.hapynes_add()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and cursor_x > 0:
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

            elif event.key == pygame.K_1 and Matcher.money >= 1000:
                Maps.MapBuilds[cursor_y][cursor_x] = 1
                Matcher.MinusMoney(1000)
                Matcher.factories += 1
                Matcher.PeoplesHapines -= 0.1
            elif event.key == pygame.K_2 and Matcher.money >= 10:
                Maps.MapBuilds[cursor_y][cursor_x] = 2
                Matcher.MinusMoney(10)
                Matcher.AddPeoples(10)
            elif event.key == pygame.K_3 and Matcher.money >= 120:
                Maps.MapBuilds[cursor_y][cursor_x] = 4
                Matcher.MinusMoney(120)
                Matcher.GasStations += 1
                Matcher.product_cost += 1
            elif event.key == pygame.K_4 and Matcher.money >= 200:
                Maps.MapBuilds[cursor_y][cursor_x] = 5
                Matcher.MinusMoney(200)
                Matcher.shops += 1
                if Matcher.PeoplesHapines <= 100:
                    Matcher.PeoplesHapines += 30
            elif event.key == pygame.K_5 and Matcher.money >= 500:
                Maps.MapBuilds[cursor_y][cursor_x] = 6
                Matcher.MinusMoney(500)
                Matcher.Volts += 100
                Matcher.generators += 1
            elif event.key == pygame.K_6 and Matcher.money >= 10000 and not IsCentreBought:
                IsCentreBought = True
                Maps.MapBuilds[cursor_y][cursor_x] = 7
                Matcher.MinusMoney(10000)
            elif event.key == pygame.K_7 and Matcher.money >= 500:
                Maps.MapBuilds[cursor_y][cursor_x] = 9
                Matcher.MinusMoney(500)
                Matcher.water_towerwers += 1

            elif event.key == pygame.K_ESCAPE:
                IsPaused = not IsPaused

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

                print(
                    f"shops: {Matcher.shops}, TotalShops: {Matcher.TotalShops}, PeoplesHapines: {Matcher.PeoplesHapines}")

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

# Cleanup
pygame.quit()
sys.exit()
