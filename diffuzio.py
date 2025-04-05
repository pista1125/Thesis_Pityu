import pygame
import math

# Constants
WIDTH, HEIGHT = 840, 600
WHITE = (255, 255, 255)
color = (0, 0, 245)
color_2 = (100, 0, 0)
BLACK = (0, 0, 0)
BALL_RADIUS = 5
INITIAL_SPEED = 3

class Ball:
    def __init__(self, x, y, radius, vx, vy):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.color = color

    def ball_place(self):
        ball_place = (self.x, self.y)
        return ball_place

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

    def update_place(self, x, y):
        self.x += x
        self.y += y

class Brick:
    def __init__(self, color, hely, sugar):
        self.color = color
        self.hely = hely
        self.sugar = sugar

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.hely, self.sugar)

    def update_color(self, update_color):
        self.color = update_color
