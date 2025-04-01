import time

import pygame
import button
import random

from diffuzio import Ball

pygame.init()
screen = pygame.display.set_mode((840, 600))
pygame.display.set_caption("Főmenű")
clock = pygame.time.Clock()


main = True
run  = True
game = None

diff_button = button.Button("Diffúzió", (0, 0, 255), (100, 100), 40)
boly_button = button.Button("Bolyongás", (0, 0, 255), (450, 100), 40)
brow_button = button.Button("Brown mozgás", (0, 0, 255), (100, 300), 40)
pass_button = button.Button("Pass", (0, 0, 255), (450, 300), 40)
exit_button = button.Button("Kilépés", (0, 0, 255), (340, 500), 40)


BALL_RADIUS = 5
INITIAL_SPEED = 3
balls = []
chemical = []
start = 0


while run:

    screen.fill((0,0,0))


    if main:
        a = diff_button.draw(screen)
        b = boly_button.draw(screen)
        c = brow_button.draw(screen)
        d = pass_button.draw(screen)
        e = exit_button.draw(screen)
#This code about main menu
        if a:
            main = False
            game = 1
            pygame.display.set_caption("Diffúzió")
        elif b:
            main = False
            game = 2
            pygame.display.set_caption("Bolyongás")
        elif c:
            main = False
            game = 3
            pygame.display.set_caption("Brown mozgás")
        elif d:
            main = False
            game = 4
            pygame.display.set_caption("pass")
        elif e:
            run = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    if game == 1:

        if start == 0:

            for x in range(300):
                balls.append(Ball(random.randint(10, 700), random.randint(10, 500), BALL_RADIUS, random.randint(1, 5),
                                  random.randint(3, 5)))

            #if I want chemical
            for x in range(10):
                balls[x].__init__(random.randint(10, 40), random.randint(10, 40), BALL_RADIUS, random.randint(1, 5),
                                  random.randint(3, 5))
                balls[x].update_color()
            start = 1

        for ball in balls:
            ball.update()
            ball.draw(screen)

                # Check collisions between balls
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].collide_with_other_ball(balls[j])

        pygame.display.flip()
        clock.tick(60)
    pygame.display.update()
