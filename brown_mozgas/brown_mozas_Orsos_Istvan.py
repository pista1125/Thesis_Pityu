import pygame
import random
import math

# Inicializáljuk a Pygame-et
pygame.init()

# Ablak méretei
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brown-mozgás")

# Színek
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
trail_color = (255, 0, 0)

# A nagy piros golyó adatai
big_ball_radius = 50
big_ball_x = width // 2
big_ball_y = height // 2
big_ball_speed = 5  # Megnövelt sebesség
big_ball_dx = random.uniform(-big_ball_speed, big_ball_speed)
big_ball_dy = random.uniform(-big_ball_speed, big_ball_speed)
trail = []
trail_length = 3000  # Meghosszabbított csík

# A kis kék golyók listája
num_small_balls = 25
small_balls = []
small_ball_radius = 10
small_ball_speed = 4  # Megnövelt sebesség

for _ in range(num_small_balls):
    while True:
        x = random.randint(small_ball_radius, width - small_ball_radius)
        y = random.randint(small_ball_radius, height - small_ball_radius)
        if math.sqrt((x - big_ball_x)**2 + (y - big_ball_y)**2) > big_ball_radius + small_ball_radius + 10:
            break
    dx = random.uniform(-small_ball_speed, small_ball_speed)
    dy = random.uniform(-small_ball_speed, small_ball_speed)
    small_balls.append([x, y, dx, dy, small_ball_radius])

def draw_ball(x, y, radius, color):
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)

def check_collision(ball1, ball2):
    x1, y1, _, _, r1 = ball1
    x2, y2, _, _, r2 = ball2
    distance_squared = (x1 - x2)**2 + (y1 - y2)**2
    radii_sum_squared = (r1 + r2)**2
    return distance_squared <= radii_sum_squared

# Játék ciklus
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Háttérszín
    screen.fill(white)

    # Nagy golyó mozgatása (Brown-mozgás)
    big_ball_x += big_ball_dx
    big_ball_y += big_ball_dy

    # Ütközés a falakkal (nagy golyó)
    if big_ball_x + big_ball_radius > width or big_ball_x - big_ball_radius < 0:
        big_ball_dx *= -1
    if big_ball_y + big_ball_radius > height or big_ball_y - big_ball_radius < 0:
        big_ball_dy *= -1

    # A mozgás véletlenszerű megváltoztatása
    if random.random() < 0.05:
        big_ball_dx += random.uniform(-1, 1)  # Nagyobb véletlenszerű változás
        big_ball_dy += random.uniform(-1, 1)
        # Sebesség korlátozása
        speed = math.sqrt(big_ball_dx**2 + big_ball_dy**2)
        if speed > big_ball_speed * 1.5:
            big_ball_dx *= big_ball_speed * 1.5 / speed
            big_ball_dy *= big_ball_speed * 1.5 / speed

    # Nagy golyó pályájának rajzolása
    trail.append((int(big_ball_x), int(big_ball_y)))
    if len(trail) > trail_length:
        trail.pop(0)
    for i, pos in enumerate(trail):
        alpha = int(255 * (i / trail_length))
        color = (trail_color[0], trail_color[1], trail_color[2], alpha)
        pygame.draw.circle(screen, color, pos, 3)

    # Kis golyók mozgatása és ütközések kezelése
    for i, ball1 in enumerate(small_balls):
        ball1[0] += ball1[2]
        ball1[1] += ball1[3]

        # Falakkal való ütközés (kis golyók)
        if ball1[0] + ball1[4] > width or ball1[0] - ball1[4] < 0:
            ball1[2] *= -1
        if ball1[1] + ball1[4] > height or ball1[1] - ball1[4] < 0:
            ball1[3] *= -1

        # Ütközés a nagy golyóval
        if check_collision([big_ball_x, big_ball_y, big_ball_dx, big_ball_dy, big_ball_radius], ball1):
            big_ball_dx *= -1
            big_ball_dy *= -1
            ball1[2] *= -1
            ball1[3] *= -1

        # Kis golyók közötti ütközések
        for j in range(i + 1, len(small_balls)):
            ball2 = small_balls[j]
            if check_collision(ball1, ball2):
                ball1[2] *= -1
                ball1[3] *= -1
                ball2[2] *= -1
                ball2[3] *= -1

    # Nagy golyó rajzolása
    draw_ball(big_ball_x, big_ball_y, big_ball_radius, red)

    # Kis golyók rajzolása
    for ball in small_balls:
        draw_ball(ball[0], ball[1], ball[4], blue)

    # Képernyő frissítése
    pygame.display.flip()

    # Késleltetés a képkockasebesség szabályozásához
    pygame.time.delay(30)

# Kilépés a Pygame-ből
pygame.quit()