import time
import pygame
import button
import random
import math
from diffuzio import Ball, Brick


GREEN = (0, 255, 0)
BlUE = (0, 0, 255)
RED = (255, 0, 0)

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
time_tittle = button.Button("00:00:00", (255,0,0), (WIDTH/2, 50), 40)
ball_box = button.Button("      ", (0,0,255), (WIDTH/2, HEIGHT/2), 40)


BALL_RADIUS = 5
INITIAL_SPEED =[-5, -4, -3, -2, 2, 3, 4, 5]
balls = []
#chemical = []
illat_labdak = 40
brick_hely = [((WIDTH / 2), (HEIGHT / 4)), ((WIDTH / 2), (HEIGHT / 4) * 3), ((WIDTH / 4), HEIGHT / 2), ((WIDTH / 4) * 3, HEIGHT / 2)]

brick_color = BlUE
akadalyok = []
catch = 0
catch_1, catch_2, catch_3, catch_4 = False, False, False, False
catch_time = []
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

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
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
        if event.type == pygame.KEYDOWN:
            if game == 1 and pause_button == 1:
                #Kezdeti mozgatás az illatmolekuláknak
                if event.key == pygame.K_RIGHT:
                    for x in range(illat_labdak):
                        balls[x].update_place(40, 0)
                        ball_box.update_place(1, 0)
                elif event.key == pygame.K_LEFT:
                    for x in range(illat_labdak):
                        balls[x].update_place(-40, 0)
                        ball_box.update_place(-1, 0)
                elif event.key == pygame.K_UP:
                    for x in range(illat_labdak):
                        balls[x].update_place(0, -40)
                        ball_box.update_place(0, -1)
                elif event.key == pygame.K_DOWN:
                    for x in range(illat_labdak):
                        balls[x].update_place(0, 40)
                        ball_box.update_place(0, 1)


    if main:
        a = diff_button.draw(screen, BlUE)
        b = boly_button.draw(screen, BlUE)
        c = brow_button.draw(screen, BlUE)
        d = pass_button.draw(screen, BlUE)
        e = exit_button.draw(screen, BlUE)
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




    if game == 1:
        screen.fill((0, 0, 0))
        #kezdő képernyő (start gomb, stopper, akadályok, labdák, illatlabdák)
        start_button.draw(screen, BlUE)
        time_tittle.draw(screen, BlUE)
        if pause_button == 1:
            ball_box.draw(screen, RED)




        if start == 0:

            for hely in brick_hely:
                akadalyok.append(Brick(brick_color, hely, 25))

            for x in range(300):
                balls.append(
                    Ball(random.randint(10, WIDTH), random.randint(10, HEIGHT), BALL_RADIUS, random.choice(INITIAL_SPEED),
                         random.choice(INITIAL_SPEED)))

            # if I want chemical
            for x in range(illat_labdak):
                balls[x].__init__(random.randint((WIDTH / 2) - 10, (WIDTH / 2) + 10),
                                  random.randint((HEIGHT / 2) - 10, (HEIGHT / 2) + 10), BALL_RADIUS,
                                  random.choice(INITIAL_SPEED),
                                  random.choice(INITIAL_SPEED))
                balls[x].update_color()

            start = 1

        #Stopper eltelt idő
        if stopper_running:
            elapsed_time = time.time() - start_time


        # Idő formázása
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 100) % 100)
        time_text = f"{minutes:02}:{seconds:02}:{milliseconds:02}"

        time_tittle.update_name(time_text)


        #akadályok megrajzolása
        for x in akadalyok:
            x.draw(screen)

        # ha megy a szimulacio, akkor mozognak a labdak
        for ball in balls:
            ball.draw(screen)
            if game1_start == True and catch < 4:
                ball.update()

                # Check collisions between balls
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].collide_with_other_ball(balls[j])
        #check collision between balls and brick
        for i in balls[:illat_labdak]:
            distance_1 = math.sqrt((i.ball_place()[0] - brick_hely[0][0]) ** 2 + (i.ball_place()[1] - brick_hely[0][1]) ** 2)
            distance_2 = math.sqrt((i.ball_place()[0] - brick_hely[1][0]) ** 2 + (i.ball_place()[1] - brick_hely[1][1]) ** 2)
            distance_3 = math.sqrt((i.ball_place()[0] - brick_hely[2][0]) ** 2 + (i.ball_place()[1] - brick_hely[2][1]) ** 2)
            distance_4 = math.sqrt((i.ball_place()[0] - brick_hely[3][0]) ** 2 + (i.ball_place()[1] - brick_hely[3][1]) ** 2)

            if distance_1 < 25 and pause_button > 1:
                akadalyok[0].update_color(RED)
                if catch_1 == False:
                    catch_1 = True
                    catch += 1
            if distance_2 < 25 and pause_button > 1:
                akadalyok[1].update_color(RED)
                if catch_2 == False:
                    catch_2 = True
                    catch += 1
            if distance_3 < 25 and pause_button > 1:
                akadalyok[2].update_color(RED)
                if catch_3 == False:
                    catch_3 = True
                    catch += 1
            if distance_4 < 25 and pause_button > 1:
                akadalyok[3].update_color(RED)
                if catch_4 == False:
                    catch_4 = True
                    catch += 1
        if catch == 4:
            stopper_running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.display.update()

pygame.quit()