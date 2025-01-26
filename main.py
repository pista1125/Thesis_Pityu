import random
import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
color = (0, 0, 245)
color_2 = (100, 0, 0)
BLACK = (0, 0, 0)
BALL_RADIUS = 5
INITIAL_SPEED = 3

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Ball Motion with Collisions")
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self, x, y, radius, vx, vy):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.color = color

    def update_color(self):
        self.color = color_2

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.vx *= -1
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collide_with_other_ball(self, other_ball):
        distance = math.sqrt((self.x - other_ball.x)**2 + (self.y - other_ball.y)**2)
        if distance <= self.radius + other_ball.radius:
            self.vx *= -1
            self.vy *= -1

# Main function
def main():
    balls = []
    chemical = []
    for x in range(300):
        balls.append(Ball(random.randint(10, 790), random.randint(10, 590), BALL_RADIUS, random.randint(1, 5), random.randint(3,5)))

    #if I want chemical
    for x in range(10):
        balls[x].__init__(random.randint(10, 40), random.randint(10, 40), BALL_RADIUS, random.randint(1, 5), random.randint(3,5))
        balls[x].update_color()

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for ball in balls:
            ball.update()
            ball.draw(screen)

        # Check collisions between balls
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].collide_with_other_ball(balls[j])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()