import time
import pygame
import button
import random
import math
from diffuzio import Ball, Brick



GREEN = (6, 206, 89)
BlUE = (0, 0, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 840, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diffúzió")
clock = pygame.time.Clock()

run  = True

#game button, text stb

font = pygame.font.Font(None, 40)
game_2_menu = True

#szovegmezo
game_2_input_box = pygame.Rect((WIDTH/2)-150, (HEIGHT/2)-150, 320, 40)
game_2_user_text = 'Piros golyók száma:'
active = False

# Gomb
game_2_input_button = pygame.Rect((WIDTH/2)-50, HEIGHT/2, 100, 40)

start_button = button.Button("Start", (255,0,0), (((WIDTH/5)*4) + 30, 100), 40)
stop_button = button.Button(" Stop ", (255,0,0), (((WIDTH/5)*4) + 28, 150), 40)
time_tittle = button.Button("              ", (255,0,0), (WIDTH/2, 50), 40)
ball_box = button.Button("      ", (0,0,10), (WIDTH/2, HEIGHT/2), 40)
ball_box_title = []

BALL_RADIUS = 5
BALL_NUMBER = 300
INITIAL_SPEED =[-5, -4, -3, -2, 2, 3, 4, 5]
balls = []
#chemical = []
illat_labdak = 40
brick_hely = [((WIDTH / 2), (HEIGHT / 4)), ((WIDTH / 2), (HEIGHT / 4) * 3), ((WIDTH / 4), HEIGHT / 2), ((WIDTH / 4) * 3, HEIGHT / 2)]

brick_color = BlUE
akadalyok = []
catch = 0
catch_1, catch_2, catch_3, catch_4 = False, False, False, False
catch_time_1, catch_time_2, catch_time_3, catch_time_4 = None, None, None, None
start = 0
pause = False
pause_button = 1
game2_start = False

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
        #game 2 menu
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Szövegmező aktiválása
            if game_2_input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
                # Gomb megnyomása
            if game_2_input_button.collidepoint(event.pos):
                game_2_menu = False
                illat_labdak = int(game_2_user_text[19:])

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    game_2_user_text = game_2_user_text[:-1]
                else:
                    game_2_user_text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if stop_button.pos.collidepoint(event.pos):
                game2_start = False
                stopper_running = False
            elif start_button.pos.collidepoint(event.pos):
                game2_start = True
                pause_button += 1
                stopper_running = True
                start_time = time.time() - elapsed_time
        if event.type == pygame.KEYDOWN:
            if pause_button == 1:
                #Kezdeti mozgatás az illatmolekuláknak
                if event.key == pygame.K_RIGHT:
                    for x in range(illat_labdak):
                        balls[x].update_place(30, 0)
                        ball_box.update_place(1, 0)
                elif event.key == pygame.K_LEFT:
                    for x in range(illat_labdak):
                        balls[x].update_place(-30, 0)
                        ball_box.update_place(-1, 0)
                elif event.key == pygame.K_UP:
                    for x in range(illat_labdak):
                        balls[x].update_place(0, -30)
                        ball_box.update_place(0, -1)
                elif event.key == pygame.K_DOWN:
                    for x in range(illat_labdak):
                        balls[x].update_place(0, 30)
                        ball_box.update_place(0, 1)
            if event.key == pygame.K_r:
                for x in balls:
                    x.update_speed()
            if event.key == pygame.K_t:
                for c in balls:
                    c.update_speed_low()

    if game_2_menu == True:

        # Szövegmező megjelenítés
        txt_surface = font.render(game_2_user_text, True, BlUE)
        pygame.draw.rect(screen, GREEN if active else BlUE, game_2_input_box, 2)
        screen.blit(txt_surface, (game_2_input_box.x + 5, game_2_input_box.y + 5))

        # Gomb megjelenítése
        pygame.draw.rect(screen, GREEN, game_2_input_button)
        screen.blit(font.render("Mehet", True, BlUE), (game_2_input_button.x + 10, game_2_input_button.y + 5))


    elif game_2_menu == False:

        screen.fill((0, 0, 0))
        #kezdő képernyő (start gomb, stopper, akadályok, labdák, illatlabdák)
        start_button.draw(screen, BlUE)
        stop_button.draw(screen, BlUE)
        time_tittle.draw(screen, BlUE)
        if pause_button == 1:
            ball_box.draw(screen, RED)

        if start == 0:
            #akadalyok megrajzolasa
            for hely in brick_hely:
                akadalyok.append(Brick(brick_color, hely, 25))
                ball_box_title.append(button.Button("    ", GREEN, (hely[0]-30, hely[1]), 30))
            #labdák megrajzolasa
            for x in range(BALL_NUMBER):
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
            if game2_start == True and catch < 4:
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
                    catch_time_1 = time_text
            if distance_2 < 25 and pause_button > 1:
                akadalyok[1].update_color(RED)
                if catch_2 == False:
                    catch_2 = True
                    catch += 1
                    catch_time_2 = time_text
            if distance_3 < 25 and pause_button > 1:
                akadalyok[2].update_color(RED)
                if catch_3 == False:
                    catch_3 = True
                    catch += 1
                    catch_time_3 = time_text
            if distance_4 < 25 and pause_button > 1:
                akadalyok[3].update_color(RED)
                if catch_4 == False:
                    catch_4 = True
                    catch += 1
                    catch_time_4 = time_text
        if catch == 4:
            stopper_running = False
        if catch_1:
            ball_box_title[0].draw_time(screen)
            ball_box_title[0].update_name(catch_time_1)
        if catch_2:
            ball_box_title[1].draw_time(screen)
            ball_box_title[1].update_name(catch_time_2)
        if catch_3:
            ball_box_title[2].draw_time(screen)
            ball_box_title[2].update_name(catch_time_3)
        if catch_4:
            ball_box_title[3].draw_time(screen)
            ball_box_title[3].update_name(catch_time_4)
        pygame.display.flip()
        clock.tick(30)
    pygame.display.update()
pygame.quit()