import pygame
import sys
import Maps
import PUi
import Matcher
import time

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_X = 1000
SCREEN_Y = 900
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("CityLab!")

# Load images
images = {
    "grass": pygame.image.load(Maps.grass).convert_alpha(),
    "sand": pygame.image.load(Maps.sand).convert_alpha(),
    "factory": pygame.image.load(Maps.factory).convert_alpha(),
    "cursor": pygame.image.load(Maps.cursor).convert_alpha(),
    "flat": pygame.image.load(Maps.Flat).convert_alpha(),
    "tree": pygame.image.load(Maps.forest).convert_alpha()
}

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

def draw_cursor():
    cell_size = Maps.CellSize
    pos = (cursor_x * cell_size, cursor_y * cell_size)
    screen.blit(images["cursor"], pos)

# Initialize cursor position
cursor_x, cursor_y = 0, 0
columns = 15
rows = 9

# Main loop
running = True
while running:
    if Matcher.factories < 0:
        Matcher.product += 1

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
            elif event.key == pygame.K_1 and Matcher.money >= 100:
                Maps.MapBuilds[cursor_y][cursor_x] = 1
                Matcher.MinusMoney(100)
                Matcher.factories += 1
            elif event.key == pygame.K_2 and Matcher.money >= 10:
                Maps.MapBuilds[cursor_y][cursor_x] = 2
                Matcher.MinusMoney(10)
                Matcher.AddPeoples(10)
            elif event.key == pygame.K_SPACE:
                if Matcher.product > 0:
                    total_sale = Matcher.product_cost * Matcher.product
                    if Matcher.money >= total_sale:
                        Matcher.product_cost += Matcher.money
                        Matcher.product = 0
                        Matcher.AddMoney(total_sale)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the map, buildings, and cursor
    draw_map()
    draw_buildings()
    draw_cursor()
    PUi.DrawUi(screen, (0, 600), Matcher.money, Matcher.peoples)

    # Update the display
    pygame.display.update()

# Cleanup
pygame.quit()
sys.exit()
