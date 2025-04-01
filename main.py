import time
import pygame
import button
import random
from diffuzio import Ball

WIDTH, HEIGHT = 840, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Főmenű")
clock = pygame.time.Clock()


main = True
run  = True
game = None

diff_button = button.Button("Diffúzió", (0, 0, 255), (WIDTH/4, 100), 40)
boly_button = button.Button("Bolyongás", (0, 0, 255), ((WIDTH/4)*3, 100), 40)
brow_button = button.Button("Brown mozgás", (0, 0, 255), (WIDTH/4, 300), 40)
pass_button = button.Button("Pass", (0, 0, 255), ((WIDTH/4)*3, 300), 40)
exit_button = button.Button("Kilépés", (0, 0, 255), (WIDTH/2, 500), 40)

#game 1 Start button

start_button = button.Button("Start", (255,0,0), ((WIDTH/5)*4, 100), 40)
time_tittle = button.Button("00:00", (255,0,0), (WIDTH/2, 50), 40)


BALL_RADIUS = 5
INITIAL_SPEED = 3
balls = []
chemical = []
start = 0
pause = False
pause_button = 1
game1_start = False

# Stopper változók
running = True
stopper_running = False
start_time = 0
elapsed_time = 0


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.pos.collidepoint(event.pos) and pause_button % 2 ==0:
                game1_start = False
                pause_button += 1
                start_button.update_name("Start")
                stopper_running = False
            elif start_button.pos.collidepoint(event.pos) and pause_button % 2 ==1:
                game1_start = True
                pause_button += 1
                start_button.update_name("Stop")
                stopper_running = True
                start_time = time.time() - elapsed_time


    if game == 1:
        screen.fill((0, 0, 0))
        start_button.draw(screen)
        time_tittle.draw(screen)
        if stopper_running:
            elapsed_time = time.time() - start_time
        # Idő formázása
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 100) % 100)
        time_text = f"{seconds:02}:{milliseconds:02}"

        time_tittle.update_name(time_text)

        if start == 0:

            for x in range(300):
                balls.append(Ball(random.randint(10, WIDTH), random.randint(10, HEIGHT), BALL_RADIUS, random.randint(1, 5),
                                  random.randint(3, 5)))

            #if I want chemical
            for x in range(10):
                balls[x].__init__(random.randint(10, 40), random.randint(10, 40), BALL_RADIUS, random.randint(1, 5),
                                  random.randint(3, 5))
                balls[x].update_color()
            start = 1
        for ball in balls:
            ball.draw(screen)
            if game1_start == True:
                ball.update()

                # Check collisions between balls
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].collide_with_other_ball(balls[j])

        pygame.display.flip()
        clock.tick(30)

    pygame.display.update()

pygame.quit()