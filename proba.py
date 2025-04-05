import pygame

pygame.init()
WIDTH, HEIGHT = 840, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
square = pygame.Rect(10, 10, 50, 50)
Run = True
while Run:

    pygame.draw.rect(screen, (0,33,255), square)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update()