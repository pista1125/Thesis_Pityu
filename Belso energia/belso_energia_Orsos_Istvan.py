import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Belső Energia Változás")

# Színek
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (30, 30, 30)
GREEN = (0, 255, 0)
RED = (255, 50, 50)
CYAN = (0, 200, 200)

# Molekula beállítások
NUM_BALLS = 300
BALL_RADIUS = 5

font = pygame.font.SysFont(None, 26)

# Kezdeti állapot
state = 'normal'

# Gombos interfész
class Button:
    def __init__(self, rect, text, color, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        label = font.render(self.text, True, WHITE)
        surface.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

# Molekula (labda) osztály
class Ball:
    def __init__(self):
        self.x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        self.y = random.randint(BALL_RADIUS + 100, HEIGHT - BALL_RADIUS)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.nyomas = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= BALL_RADIUS or self.x >= WIDTH -  + BALL_RADIUS:
            self.vx *= -1
        if self.y <= BALL_RADIUS + 100 or self.y >= HEIGHT - BALL_RADIUS:
            self.vy *= -1




    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), BALL_RADIUS)

    def set_speed_multiplier(self, multiplier):
        self.vx *= multiplier
        self.vy *= multiplier

    def stop(self):
        self.vx = 0
        self.vy = 0

balls = [Ball() for _ in range(NUM_BALLS)]

# Gombok
def set_hot():
    global state
    state = 'hot'
    for b in balls:
        b.set_speed_multiplier(1.5)
def set_cold():
    global state
    state = 'cold'
    for b in balls:
        b.set_speed_multiplier(0.5)

def set_freeze():
    global state
    state = 'freeze'
    for b in balls:
        b.stop()

def reset_sim():
    global state, balls
    state = 'normal'
    balls = [Ball() for _ in range(NUM_BALLS)]

buttons = [
    Button((20, 20, 120, 40), "Gyertya", RED, set_hot),
    Button((160, 20, 120, 40), "Jég", CYAN, set_cold),
    Button((300, 20, 150, 40), "Fagyasztó", GRAY, set_freeze),
    Button((470, 20, 120, 40), "Reset", GREEN, reset_sim),
]

# Hőmérséklet becslés
def get_avg_speed():
    total = sum((abs(b.vx) + abs(b.vy)) for b in balls)
    return total / (2 * len(balls))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Események
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                btn.check_click(event.pos)

    # Mozgatás
    if state != 'freeze':
        for b in balls:
            b.move()

    # Kirajzolás
    for b in balls:
        b.draw(screen)

    # Gombok
    for btn in buttons:
        btn.draw(screen)

    # Hőmérséklet kijelző
    avg_speed = get_avg_speed()
    temp = int(avg_speed * 100)
    pygame.draw.rect(screen, WHITE, (650, 20, 200, 40), border_radius=10)
    pygame.draw.rect(screen, RED, (650, 20, min(temp * 2, 200), 40), border_radius=10)
    temp_text = font.render(f"Hőmérséklet: {temp} K", True, BLACK)
    screen.blit(temp_text, (660, 30))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()