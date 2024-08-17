import pygame

import pygame


def DrawUi(screen, position, money, peoples):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(position, (1200, 300)))
    font = pygame.font.SysFont(None, 48)

    money_text = "$ : " + str(money)
    peoples_text = "peoples : " + str(peoples)
    products_text = "products : " + str(peoples)

    money_surface = font.render(money_text, True, (255, 255, 255))
    peoples_surface = font.render(peoples_text, True, (255, 255, 255))
    products_surface = font.render(products_text, True, (255, 255, 255))

    money_rect = money_surface.get_rect(topleft=(position[0] + 10, position[1] + 10))
    peoples_rect = peoples_surface.get_rect(topleft=(position[0] + 10, position[1] + 50))
    products_rect = products_surface.get_rect(topleft=(position[0] + 10, position[1] + 90))

    screen.blit(money_surface, money_rect)
    screen.blit(peoples_surface, peoples_rect)
    screen.blit(products_surface, products_rect)

