import pygame

class Button():
    def __init__(self, text, color, pos, size):
        self.color = color
        self.font = pygame.font.SysFont("Times New Roman", size)
        self.text = self.font.render(text, True, self.color)
        self.pos = pos
        self.pos =self.text.get_rect(center=self.pos)

    def draw(self, screen, rect_color):
        action = False
        self.blit = screen.blit(self.text, self.pos)
        pygame.draw.rect(screen, (rect_color), self.pos, 3)

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.pos.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        return action

    def update_name(self, text):
        self.text = self.font.render(text, True, self.color)

    def update_place(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def draw_time(self, screen):
        self.blit = screen.blit(self.text, self.pos)