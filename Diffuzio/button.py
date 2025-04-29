import pygame


GREEN = (6, 206, 89)

class Button():
    def __init__(self, text, color, pos, size):
        self.color = color
        self.texting = text
        self.font = pygame.font.SysFont("Times New Roman", size)
        self.text = self.font.render(text, True, self.color)
        self.pos = pos
        self.pos =self.text.get_rect(center=self.pos)

    def draw(self, screen, rect_color):
        action = False
        pos = pygame.mouse.get_pos()

        if self.pos.collidepoint(pos):
            self.color = GREEN
            self.blit = screen.blit(self.text, self.pos)
            self.text = self.font.render(self.texting, True, self.color)
            pygame.draw.rect(screen, rect_color, self.pos, 3)
        else:
            self.color = (0, 0, 255)
            self.blit = screen.blit(self.text, self.pos)
            pygame.draw.rect(screen, rect_color, self.pos, 3)
            self.text = self.font.render(self.texting, True, self.color)

        # self.blit = screen.blit(self.text, self.pos)
        # pygame.draw.rect(screen, (rect_color), self.pos, 3)

        # get mouse position

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