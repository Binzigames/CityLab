import pygame
import Matcher
def DrawUi(screen, position, money, peoples, products, eco, happiness, volts, water):
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
        f"happiness : %{happiness}",
        f"Volts : {volts}",
        f"Water : {water}"
    ]

    positions = [
        (position[0] + 10, position[1] + 10),
        (position[0] + 10, position[1] + 50),
        (position[0] + 10, position[1] + 90),
        (position[0] + 10, position[1] + 130),
        (position[0] + 10, position[1] + 170),
        (position[0] + 10, position[1] + 210),
        (position[0] + 10, position[1] + 250)
    ]

    # Render and draw each text surface
    for text, pos in zip(texts, positions):
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=pos)
        screen.blit(text_surface, text_rect)

def DrawPicture(screen, position, ecology):
    try:
        # Load images correctly (without comma to avoid creating tuples)
        StandartPanorama = pygame.image.load("panarama_city.png").convert_alpha()
        DirtyPanorama = pygame.image.load("panarama_dirty_city.png").convert_alpha()
    except pygame.error as e:
        print(f"Unable to load image: {e}")
        return

    # Determine which panorama to use
    if ecology < 20:
        corect_panarama = DirtyPanorama
    else:
        corect_panarama = StandartPanorama


    scaled_image = pygame.transform.scale(corect_panarama, (480, 300))


    picture_position = (position[0] + 500, position[1])


    screen.blit(scaled_image, picture_position)

