

white = (0,0,0)


import pygame
import button

pygame.init()


screen = pygame.display.set_mode((840, 600))
pygame.display.set_caption("Főmenű")

main = True
run  = True
game = None
while run:

    screen.fill((0,0,0))

    diff_button = button.Button("Diffúzió", (0, 0, 255), (100, 100), 40)
    boly_button = button.Button("Bolyongás", (0, 0, 255), (450, 100), 40)
    brow_button = button.Button("Brown mozgás", (0, 0, 255), (100, 300), 40)
    pass_button = button.Button("Pass", (0, 0, 255), (450, 300), 40)
    exit_button = button.Button("Kilépés", (0, 0, 255), (340, 500), 40)
    if main:
        a = diff_button.draw(screen)
        b = boly_button.draw(screen)
        c = brow_button.draw(screen)
        d = pass_button.draw(screen)
        e = exit_button.draw(screen)

        if a:
            main = False
            game = 1
        elif b:
            main = False
            game = 2
        elif c:
            main = False
            game = 3
        elif d:
            main = False
            game = 4
    if game == 1:
        pygame.display.set_caption("Diffúzió")

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    pygame.display.update()
