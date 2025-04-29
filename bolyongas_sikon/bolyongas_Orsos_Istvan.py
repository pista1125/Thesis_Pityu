import pygame
import random

pygame.init()

# Alap beállítások
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Számegyenes Dobókockás Játék")

FONT = pygame.font.SysFont("Arial", 24)
BIGFONT = pygame.font.SysFont("Arial", 36)

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)

# Számegyenes paraméterek
START_X = 100
END_X = WIDTH - 100
LINE_Y = HEIGHT // 2
NUM_POSITIONS = 21  # -10 ... 0 ... +10
SPACING = (END_X - START_X) // (NUM_POSITIONS - 1)

# Golyó pozíciója (kezdetben 0-nál)
position = 10  # 0 indexe = 10

# Dobókocka méret és hely
dice_rect = pygame.Rect(WIDTH - 120, 20, 80, 80)
last_roll = None


# Segédfüggvény
def draw():
    WIN.fill(WHITE)

    # Számegyenes
    for i in range(NUM_POSITIONS):
        x = START_X + i * SPACING
        pygame.draw.line(WIN, BLACK, (x, LINE_Y - 5), (x, LINE_Y + 5), 2)
        label = FONT.render(str(i - 10), True, BLACK)
        WIN.blit(label, (x - label.get_width() // 2, LINE_Y + 10))

    # Fő vonal
    pygame.draw.line(WIN, BLACK, (START_X, LINE_Y), (END_X, LINE_Y), 2)

    # Golyó
    ball_x = START_X + position * SPACING
    pygame.draw.circle(WIN, BLUE, (ball_x, LINE_Y - 30), 15)

    # Dobókocka
    pygame.draw.rect(WIN, RED, dice_rect)
    pygame.draw.rect(WIN, BLACK, dice_rect, 2)
    if last_roll is not None:
        roll_text = BIGFONT.render(str(last_roll), True, WHITE)
        WIN.blit(roll_text,
                 (dice_rect.centerx - roll_text.get_width() // 2, dice_rect.centery - roll_text.get_height() // 2))
    else:
        roll_text = FONT.render("Dobj!", True, WHITE)
        WIN.blit(roll_text,
                 (dice_rect.centerx - roll_text.get_width() // 2, dice_rect.centery - roll_text.get_height() // 2))

    pygame.display.update()


# Fő ciklus
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if dice_rect.collidepoint(event.pos):
                roll = random.randint(1, 6)
                last_roll = roll
                if roll % 2 == 0:
                    if position < NUM_POSITIONS - 1:
                        position += 1
                else:
                    if position > 0:
                        position -= 1

pygame.quit()

#
# import pygame
# import random
#
# pygame.init()
#
# # Ablak méret
# WIDTH, HEIGHT = 1000, 600
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Számegyenes Statisztikai Szimuláció")
#
# FONT = pygame.font.SysFont("Arial", 20)
# BIGFONT = pygame.font.SysFont("Arial", 28)
#
# # Színek
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
# RED = (200, 50, 50)
# GRAY = (180, 180, 180)
#
# # Számegyenes beállításai
# START_X = 100
# END_X = WIDTH - 100
# LINE_Y = HEIGHT // 2
# SPACING = (END_X - START_X) // 20  # Csökkentve, mivel nincsenek határok
#
# # Dobáskocka gomb
# dice_rect = pygame.Rect(WIDTH - 140, 20, 100, 50)
# simulate_rect = pygame.Rect(WIDTH - 140, 90, 100, 40)
#
# # Pozíciók és statisztika
# position = 10  # induló pozíció (0 indexe = 10)
# last_roll = None
# position_counts = {}
#
# simulation_done = False
#
#
# def draw_main():
#     WIN.fill(WHITE)
#
#     # Számegyenes
#     for i in range(-10, 11):  # Most már a teljes számegyenest megjelenítjük
#         x = START_X + (i + 10) * SPACING  # -10 ... +10
#         pygame.draw.line(WIN, BLACK, (x, LINE_Y - 5), (x, LINE_Y + 5), 2)
#         label = FONT.render(str(i), True, BLACK)
#         WIN.blit(label, (x - label.get_width() // 2, LINE_Y + 10))
#
#     pygame.draw.line(WIN, BLACK, (START_X, LINE_Y), (END_X, LINE_Y), 2)
#
#     # Golyó kirajzolása
#     ball_x = START_X + (position + 10) * SPACING
#     pygame.draw.circle(WIN, BLUE, (ball_x, LINE_Y - 30), 15)
#
#     # Dobókocka gomb
#     pygame.draw.rect(WIN, RED, dice_rect)
#     pygame.draw.rect(WIN, BLACK, dice_rect, 2)
#     dice_text = BIGFONT.render("Dobás", True, WHITE)
#     WIN.blit(dice_text,
#              (dice_rect.centerx - dice_text.get_width() // 2, dice_rect.centery - dice_text.get_height() // 2))
#
#     # Szimuláció gomb
#     pygame.draw.rect(WIN, GRAY, simulate_rect)
#     pygame.draw.rect(WIN, BLACK, simulate_rect, 2)
#     sim_text = FONT.render("100 dobás", True, BLACK)
#     WIN.blit(sim_text,
#              (simulate_rect.centerx - sim_text.get_width() // 2, simulate_rect.centery - sim_text.get_height() // 2))
#
#     pygame.display.update()
#
#
# def draw_statistics():
#     WIN.fill(WHITE)
#
#     max_count = max(position_counts.values(), default=1)
#     chart_bottom = HEIGHT - 50
#     chart_top = 50
#     chart_height = chart_bottom - chart_top
#
#     # Tengely + oszlopok
#     for pos, count in position_counts.items():
#         x = START_X + (pos + 10) * SPACING
#         height_ratio = count / max_count if max_count > 0 else 0
#         bar_height = height_ratio * chart_height
#         y = chart_bottom - bar_height
#         pygame.draw.rect(WIN, BLUE, (x - 10, y, 20, bar_height))
#
#         label = FONT.render(str(pos), True, BLACK)
#         WIN.blit(label, (x - label.get_width() // 2, chart_bottom + 5))
#         count_label = FONT.render(str(count), True, BLACK)
#         WIN.blit(count_label, (x - count_label.get_width() // 2, y - 20))
#
#     pygame.draw.line(WIN, BLACK, (START_X, chart_bottom), (END_X, chart_bottom), 2)
#
#     pygame.display.update()
#
#
# # Dobás logikája
# def do_roll():
#     global position, last_roll
#     roll = random.randint(1, 6)
#     last_roll = roll
#     if roll % 2 == 0:  # Páros, jobbra
#         position += 1
#     else:  # Páratlan, balra
#         position -= 1
#
#     if position not in position_counts:
#         position_counts[position] = 0
#     position_counts[position] += 1
#
#
# # Szimuláció
# def simulate_rolls(n=10000):
#     global position
#     position = 10  # reset
#     for i in range(n):
#         do_roll()
#
#
# # Fő ciklus
# run = True
# clock = pygame.time.Clock()
#
# while run:
#     clock.tick(30)
#
#     if simulation_done:
#         draw_statistics()
#     else:
#         draw_main()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if dice_rect.collidepoint(event.pos) and not simulation_done:
#                 do_roll()
#             elif simulate_rect.collidepoint(event.pos):
#                 simulate_rolls(10000)
#                 simulation_done = True
#
# pygame.quit()