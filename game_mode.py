

# Labda osztály
# class Ball:
#     def __init__(self, x, y, color, radius=5):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.radius = radius
#         self.dx = random.choice([-2, 2])
#         self.dy = random.choice([-2, 2])
#
#     def move(self):
#         self.x += self.dx
#         self.y += self.dy
#
#         # Falakhoz ütközés
#         if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
#             self.dx *= -1
#         if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
#             self.dy *= -1
#
#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#
#     def collide(self, other):
#         distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
#         return distance <= self.radius + other.radius
#
# # Labdák listája
# balls = []
# num_balls = 200
#
# # Fekete labdák létrehozása
# for _ in range(num_balls):
#     x = random.randint(0, WIDTH)
#     y = random.randint(0, HEIGHT)
#     balls.append(Ball(x, y, BLACK))
#
# # Piros labda létrehozása
# red_ball = Ball(0, 0, RED)
# balls.append(red_ball)
#
# # Számláló a piros labdák számára
# red_count = 1
#
# # Fő ciklus
# running = True
# clock = pygame.time.Clock()
#
# while running:
#     screen.fill(WHITE)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Labdák mozgatása és ütközés ellenőrzése
#     for ball in balls:
#         ball.move()
#         ball.draw(screen)
#
#         if ball.color == RED:
#             for other in balls:
#                 if other.color == BLACK and ball.collide(other):
#                     other.color = RED
#                     red_count += 1
#
#     # Számláló megjelenítése
#     font = pygame.font.SysFont(None, 55)
#     text = font.render(f'Piros labdák: {red_count}', True, BLACK)
#     screen.blit(text, (10, 10))
#
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()

# import pygame
# import random
# import math
# import matplotlib.pyplot as plt
# import time
#
# # Inicializálás
# pygame.init()
#
# # Ablak mérete
# WIDTH, HEIGHT = 1000, 800
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Fertőzés Játék")
#
# # Színek
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
#
# # Labda osztály
# class Ball:
#     def __init__(self, x, y, color, radius=5):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.radius = radius
#         self.dx = random.choice([-2, 2])
#         self.dy = random.choice([-2, 2])
#
#     def move(self):
#         self.x += self.dx
#         self.y += self.dy
#
#         # Falakhoz ütközés
#         if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
#             self.dx *= -1
#         if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
#             self.dy *= -1
#
#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#
#     def collide(self, other):
#         distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
#         return distance <= self.radius + other.radius
#
# # Labdák listája
# balls = []
# num_balls = 400
#
# # Fekete labdák létrehozása
# for _ in range(num_balls):
#     x = random.randint(0, WIDTH)
#     y = random.randint(0, HEIGHT)
#     balls.append(Ball(x, y, BLACK))
#
# # Piros labda létrehozása
# red_ball = Ball(0, 0, RED)
# balls.append(red_ball)
#
# # Számláló a piros labdák számára
# red_count = 1
#
# # Időmérő és adatok rögzítése
# start_time = time.time()
# time_data = []
# red_count_data = []
#
# # Fő ciklus
# running = True
# clock = pygame.time.Clock()
#
# while running:
#     screen.fill(WHITE)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Labdák mozgatása és ütközés ellenőrzése
#     for ball in balls:
#         ball.move()
#         ball.draw(screen)
#
#         if ball.color == RED:
#             for other in balls:
#                 if other.color == BLACK and ball.collide(other):
#                     other.color = RED
#                     red_count += 1
#
#     # Adatok rögzítése
#     current_time = time.time() - start_time
#     time_data.append(current_time)
#     red_count_data.append(red_count)
#
#     # Számláló megjelenítése
#     font = pygame.font.SysFont(None, 55)
#     text = font.render(f'Piros labdák: {red_count}', True, BLACK)
#     screen.blit(text, (10, 10))
#
#     pygame.display.flip()
#     clock.tick(60)
#
#     # Játék vége, ha minden labda piros
#     if red_count >= num_balls + 1:
#         running = False
#
# pygame.quit()
#
# # Grafikon készítése
# plt.figure(figsize=(10, 6))
# plt.plot(time_data, red_count_data, label="Piros labdák száma", color="red")
# plt.xlabel("Idő (másodperc)")
# plt.ylabel("Piros labdák száma")
# plt.title("Piros labdák száma az idő függvényében")
# plt.legend()
# plt.grid(True)
# plt.show()


import pygame
import random
import math
import matplotlib.pyplot as plt
import time
import sys

# Inicializálás
pygame.init()

# Ablak mérete
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Főmenű")

# Színek
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Betűtípusok
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)


# Kezdőképernyő
def start_screen():
    screen.fill(WHITE)
    width_input = InputBox(100, 100, 200, 50, "Szélesség (1000)")
    height_input = InputBox(100, 200, 200, 50, "Magasság (800)")
    ball_input = InputBox(100, 300, 200, 50, "Labdák száma (400)")
    red_ball_input = InputBox(100, 400, 200, 50, "Piros labdák (1)")
    start_button = Button(100, 500, 200, 50, "Start", GREEN)

    input_boxes = [width_input, height_input, ball_input, red_ball_input]
    buttons = [start_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in input_boxes:
                box.handle_event(event)
            for button in buttons:
                if button.handle_event(event):
                    width = int(width_input.text) if width_input.text else 1000
                    height = int(height_input.text) if height_input.text else 800
                    num_balls = int(ball_input.text) if ball_input.text else 400
                    num_red_balls = int(red_ball_input.text) if red_ball_input.text else 1
                    return width, height, num_balls, num_red_balls

        for box in input_boxes:
            box.update()
        for button in buttons:
            button.draw(screen)

        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()


# Játék fő része
def main_game(width, height, num_balls, num_red_balls):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fertőzés Játék")

    # Labda osztály
    class Ball:
        def __init__(self, x, y, color, radius=5):
            self.x = x
            self.y = y
            self.color = color
            self.radius = radius
            self.dx = random.choice([-2, 2])
            self.dy = random.choice([-2, 2])

        def move(self):
            self.x += self.dx
            self.y += self.dy

            # Falakhoz ütközés
            if self.x - self.radius < 0 or self.x + self.radius > width:
                self.dx *= -1
            if self.y - self.radius < 0 or self.y + self.radius > height:
                self.dy *= -1

        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        def collide(self, other):
            distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
            return distance <= self.radius + other.radius

    # Labdák listája
    balls = []

    # Fekete labdák létrehozása
    for _ in range(num_balls):
        x = random.randint(0, width)
        y = random.randint(0, height)
        balls.append(Ball(x, y, BLACK))

    # Piros labdák létrehozása
    for _ in range(num_red_balls):
        x = random.randint(0, width)
        y = random.randint(0, height)
        balls.append(Ball(x, y, RED))

    # Számláló a piros labdák számára
    red_count = num_red_balls

    # Időmérő és adatok rögzítése
    start_time = time.time()
    time_data = []
    red_count_data = []

    # Fő ciklus
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Labdák mozgatása és ütközés ellenőrzése
        for ball in balls:
            ball.move()
            ball.draw(screen)

            if ball.color == RED:
                for other in balls:
                    if other.color == BLACK and ball.collide(other):
                        other.color = RED
                        red_count += 1

        # Adatok rögzítése
        current_time = time.time() - start_time
        time_data.append(current_time)
        red_count_data.append(red_count)

        # Számláló megjelenítése
        text = font.render(f'Piros labdák: {red_count}', True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

        # Játék vége, ha minden labda piros
        if red_count >= num_balls + num_red_balls:
            running = False

    return time_data, red_count_data


# Eredmények megjelenítése
def show_results(time_data, red_count_data):
    plt.figure(figsize=(10, 6))
    plt.plot(time_data, red_count_data, label="Piros labdák száma", color="red")
    plt.xlabel("Idő (másodperc)")
    plt.ylabel("Piros labdák száma")
    plt.title("Piros labdák száma az idő függvényében")
    plt.legend()
    plt.grid(True)
    plt.show()


# Főmenü
def main_menu():
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Főmenü")
    start_button = Button(400, 300, 200, 50, "Start", GREEN)
    results_button = Button(400, 400, 200, 50, "Eredmények", GRAY)

    buttons = [start_button, results_button]

    time_data = []
    red_count_data = []

    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                if button.handle_event(event):
                    if button.text == "Start":
                        width, height, num_balls, num_red_balls = start_screen()
                        time_data, red_count_data = main_game(width, height, num_balls, num_red_balls)
                    elif button.text == "Eredmények":
                        if time_data and red_count_data:
                            show_results(time_data, red_count_data)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()


# InputBox osztály a beviteli mezőkhöz
class InputBox:
    def __init__(self, x, y, w, h, placeholder):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = ""
        self.placeholder = placeholder
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = RED if self.active else GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = GRAY
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = small_font.render(self.text if self.text else self.placeholder, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


# Button osztály a gombokhoz
class Button:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = small_font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))


# Főprogram indítása
if __name__ == "__main__":
    main_menu()


# Betűtípusok

# def get_font(size):  # Returns Press-Start-2P in the desired size
#     return pygame.font.Font(None, size)
#
#
# def play():
#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()
#
#         SCREEN.fill("black")
#
#         PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
#         PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(PLAY_TEXT, PLAY_RECT)
#
#         PLAY_BACK = Button(image=None, pos=(640, 460),
#                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
#
#         PLAY_BACK.changeColor(PLAY_MOUSE_POS)
#         PLAY_BACK.update(SCREEN)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
#                     main_menu()
#
#         pygame.display.update()
#
#
# def options():
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
#
#         SCREEN.fill("white")
#
#         OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
#
#         OPTIONS_BACK = Button(image=None, pos=(640, 460),
#                               text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
#
#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()
#
#         pygame.display.update()
#
#
# def main_menu():
#     while True:
#         SCREEN.fill(BLACK)
#         MENU_MOUSE_POS = pygame.mouse.get_pos()
#
#         MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
#         MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
#
#         PLAY_BUTTON = Button(image=None, pos=(640, 250),
#                              text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         OPTIONS_BUTTON = Button(image=None, pos=(640, 400),
#                                 text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         QUIT_BUTTON = Button(image=None, pos=(640, 550),
#                              text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#
#         SCREEN.blit(MENU_TEXT, MENU_RECT)
#
#         for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
#             button.changeColor(MENU_MOUSE_POS)
#             button.update(SCREEN)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     play()
#                 if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     options()
#                 if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     pygame.quit()
#                     sys.exit()
#
#         pygame.display.update()
#
#
# main_menu()

# import pygame
# import button
#
# pygame.init()
#
# #create game window
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
#
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Main Menu")

# #game variables
# menu_state = "main"
#
# #define fonts
# font = pygame.font.SysFont("arialblack", 40)
#
# #define colours
# TEXT_COL = (255, 255, 255)
#
#
# #create button instances
# resume_button = button.Button(304, 125, )
# options_button = button.Button(297, 250, options_img, 1)
# quit_button = button.Button(336, 375, quit_img, 1)
# video_button = button.Button(226, 75, video_img, 1)
# audio_button = button.Button(225, 200, audio_img, 1)
# keys_button = button.Button(246, 325, keys_img, 1)
# back_button = button.Button(332, 450, back_img, 1)
#
# def draw_text(text, font, text_col, x, y):
#   img = font.render(text, True, text_col)
#   screen.blit(img, (x, y))
#
# #game loop
# run = True
# while run:
#
#   screen.fill((52, 78, 91))
#
#   #check if game is paused
#   if game_paused == True:
#     #check menu state
#     if menu_state == "main":
#       #draw pause screen buttons
#       if resume_button.draw(screen):
#         game_paused = False
#       if options_button.draw(screen):
#         menu_state = "options"
#       if quit_button.draw(screen):
#         run = False
#     #check if the options menu is open
#     if menu_state == "options":
#       #draw the different options buttons
#       if video_button.draw(screen):
#         print("Video Settings")
#       if audio_button.draw(screen):
#         print("Audio Settings")
#       if keys_button.draw(screen):
#         print("Change Key Bindings")
#       if back_button.draw(screen):
#         menu_state = "main"
#   else:
#     draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)
#
#   #event handler
#   for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_SPACE:
#         game_paused = True
#     if event.type == pygame.QUIT:
#       run = False
#
#   pygame.display.update()
#
# pygame.quit()

    # input_boxes = [width_input, height_input, ball_input, red_ball_input]
    # buttons = [start_button]
    #
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         for box in input_boxes:
    #             box.handle_event(event)
    #         for button in buttons:
    #             if button.handle_event(event):
    #                 width = int(width_input.text) if width_input.text else 1000
    #                 height = int(height_input.text) if height_input.text else 800
    #                 num_balls = int(ball_input.text) if ball_input.text else 400
    #                 num_red_balls = int(red_ball_input.text) if red_ball_input.text else 1
    #                 return width, height, num_balls, num_red_balls
    #
    #     for box in input_boxes:
    #         box.update()
    #     for button in buttons:
    #         button.draw(screen)
    #
    #     for box in input_boxes:
    #         box.draw(screen)
    #
    #     pygame.display.flip()

# # Játék fő része
# def main_game(width, height, num_balls, num_red_balls):
#     screen = pygame.display.set_mode((width, height))
#     pygame.display.set_caption("Fertőzés Játék")

#     # Labda osztály
#     class Ball:
#         def __init__(self, x, y, color, radius=5):
#             self.x = x
#             self.y = y
#             self.color = color
#             self.radius = radius
#             self.dx = random.choice([-2, 2])
#             self.dy = random.choice([-2, 2])
#
#         def move(self):
#             self.x += self.dx
#             self.y += self.dy
#
#             # Falakhoz ütközés
#             if self.x - self.radius < 0 or self.x + self.radius > width:
#                 self.dx *= -1
#             if self.y - self.radius < 0 or self.y + self.radius > height:
#                 self.dy *= -1
#
#         def draw(self, screen):
#             pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#
#         def collide(self, other):
#             distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
#             return distance <= self.radius + other.radius
#
#     # Labdák listája
#     balls = []
#
#     # Fekete labdák létrehozása
#     for _ in range(num_balls):
#         x = random.randint(0, width)
#         y = random.randint(0, height)
#         balls.append(Ball(x, y, BLACK))
#
#     # Piros labdák létrehozása
#     for _ in range(num_red_balls):
#         x = random.randint(0, width)
#         y = random.randint(0, height)
#         balls.append(Ball(x, y, RED))
#
#     # Számláló a piros labdák számára
#     red_count = num_red_balls
#
#     # Időmérő és adatok rögzítése
#     start_time = time.time()
#     time_data = []
#     red_count_data = []
#
#     # Fő ciklus
#     running = True
#     clock = pygame.time.Clock()
#
#     while running:
#         screen.fill(WHITE)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#         # Labdák mozgatása és ütközés ellenőrzése
#         for ball in balls:
#             ball.move()
#             ball.draw(screen)
#
#             if ball.color == RED:
#                 for other in balls:
#                     if other.color == BLACK and ball.collide(other):
#                         other.color = RED
#                         red_count += 1
#
#         # Adatok rögzítése
#         current_time = time.time() - start_time
#         time_data.append(current_time)
#         red_count_data.append(red_count)
#
#         # Számláló megjelenítése
#         text = font.render(f'Piros labdák: {red_count}', True, BLACK)
#         screen.blit(text, (10, 10))
#
#         pygame.display.flip()
#         clock.tick(60)
#
#         # Játék vége, ha minden labda piros
#         if red_count >= num_balls + num_red_balls:
#             running = False
#
#     return time_data, red_count_data
#
# # Eredmények megjelenítése
# def show_results(time_data, red_count_data):
#     plt.figure(figsize=(10, 6))
#     plt.plot(time_data, red_count_data, label="Piros labdák száma", color="red")
#     plt.xlabel("Idő (másodperc)")
#     plt.ylabel("Piros labdák száma")
#     plt.title("Piros labdák száma az idő függvényében")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
# # Főmenü
# def main_menu():
#     screen = pygame.display.set_mode((1000, 800))
#     pygame.display.set_caption("Főmenü")
#     start_button = Button(400, 300, 200, 50, "Start", GREEN)
#     results_button = Button(400, 400, 200, 50, "Eredmények", GRAY)
#
#     buttons = [start_button, results_button]
#
#     time_data = []
#     red_count_data = []
#
#     while True:
#         screen.fill(WHITE)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             for button in buttons:
#                 if button.handle_event(event):
#                     if button.text == "Start":
#                         width, height, num_balls, num_red_balls = start_screen()
#                         time_data, red_count_data = main_game(width, height, num_balls, num_red_balls)
#                     elif button.text == "Eredmények":
#                         if time_data and red_count_data:
#                             show_results(time_data, red_count_data)
#
#         for button in buttons:
#             button.draw(screen)
#
#         pygame.display.flip()
#
# # InputBox osztály a beviteli mezőkhöz
# class InputBox:
#     def __init__(self, x, y, w, h, placeholder):
#         self.rect = pygame.Rect(x, y, w, h)
#         self.color = GRAY
#         self.text = ""
#         self.placeholder = placeholder
#         self.active = False
#
#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if self.rect.collidepoint(event.pos):
#                 self.active = not self.active
#             else:
#                 self.active = False
#             self.color = RED if self.active else GRAY
#         if event.type == pygame.KEYDOWN:
#             if self.active:
#                 if event.key == pygame.K_RETURN:
#                     self.active = False
#                     self.color = GRAY
#                 elif event.key == pygame.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += event.unicode
#
#     def update(self):
#         pass
#
#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, self.rect, 2)
#         text_surface = small_font.render(self.text if self.text else self.placeholder, True, BLACK)
#         screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
#
# # Button osztály a gombokhoz
# class Button:
#     def __init__(self, x, y, w, h, text, color):
#         self.rect = pygame.Rect(x, y, w, h)
#         self.color = color
#         self.text = text
#
#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if self.rect.collidepoint(event.pos):
#                 return True
#         return False
#
#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, self.rect)
#         text_surface = small_font.render(self.text, True, BLACK)
#         screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))
#
# # Főprogram indítása
# if __name__ == "__main__":
#     main_menu()



# class Button():
# 	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
# 		self.image = image
# 		self.x_pos = pos[0]
# 		self.y_pos = pos[1]
# 		self.font = font
# 		self.base_color, self.hovering_color = base_color, hovering_color
# 		self.text_input = text_input
# 		self.text = self.font.render(self.text_input, True, self.base_color)
# 		if self.image is None:
# 			self.image = self.text
# 		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
# 		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
#
# 	def update(self, screen):
# 		if self.image is not None:
# 			screen.blit(self.image, self.rect)
# 		screen.blit(self.text, self.text_rect)
#
# 	def checkForInput(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			return True
# 		return False
#
# 	def changeColor(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			self.text = self.font.render(self.text_input, True, self.hovering_color)
# 		else:
# 			self.text = self.font.render(self.text_input, True, self.base_color)
#
import pygame

#button class
class Button():
	def __init__(self, x, y, text_input, font):
		self.font = font
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True)
		self.text_rect = self.text.get_rect(center=(0, 1))
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action