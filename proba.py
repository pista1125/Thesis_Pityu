import pygame
import time

# Inicializálás
pygame.init()

# Képernyő beállítása
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stopper")
clock = pygame.time.Clock()

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Betűtípus beállítása
font = pygame.font.Font(None, 60)

# Stopper változók
running = True
stopper_running = False
start_time = 0
elapsed_time = 0

# Gomb méretei
button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 60, 100, 40)


def draw_button():
    pygame.draw.rect(screen, BLUE, button_rect)
    text = pygame.font.Font(None, 30).render("Start", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)


# Fő ciklus
while running:
    screen.fill(WHITE)

    if stopper_running:
        elapsed_time = time.time() - start_time

    # Idő formázása
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time * 100) % 100)
    time_text = f"{minutes:02}:{seconds:02}:{milliseconds:02}"

    # Idő kirajzolása
    text_surface = font.render(time_text, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    draw_button()

    # Eseménykezelés
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if not stopper_running:
                    start_time = time.time() - elapsed_time
                    stopper_running = True

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
