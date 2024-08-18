import pygame

import pygame

import pygame


def DrawUi(screen, position, money, peoples, products, eco, happiness , volts):
    """
    Draws the user interface on the screen, displaying the current stats.

    Args:
        screen (pygame.Surface): The Pygame screen surface to draw on.
        position (tuple): The (x, y) position to start drawing the UI.
        money (int): The amount of money.
        peoples (int): The number of people.
        products (int): The number of products.
        eco (int): The eco percentage.
        happiness (int): The happiness percentage.
    """
    # Draw background rectangle
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(position, (1200, 300)))

    # Define font
    font = pygame.font.SysFont(None, 48)

    # Define text data
    texts = [
        f"$ : {money}",
        f"peoples : {peoples}",
        f"products : {products}",
        f"eco : %{eco}",
        f"hapynes : %{happiness}",
        f"Volts : {volts}"
    ]

    positions = [
        (position[0] + 10, position[1] + 10),
        (position[0] + 10, position[1] + 50),
        (position[0] + 10, position[1] + 90),
        (position[0] + 10, position[1] + 130),
        (position[0] + 700, position[1] + 10),
        (position[0] + 700, position[1] + 50)
    ]

    # Render and draw each text surface
    for text, pos in zip(texts, positions):
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=pos)
        screen.blit(text_surface, text_rect)


