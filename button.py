import pygame

class Button():
    def __init__(self, text, color, pos, size):
        self.font = pygame.font.SysFont("Times New Roman", size)
        self.text = self.font.render(text, True, color)
        self.pos =self.text.get_rect(topleft=pos)

    def draw(self, screen):
        action = False
        self.blit = screen.blit(self.text, self.pos)
        pygame.draw.rect(screen, (0, 0, 255), self.pos, 2)

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.pos.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        return action