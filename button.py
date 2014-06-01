import pygame, random, sys
from pygame.locals import *

class Button(object):
    def __init__(self, surface, color, x, y, length, height, width, text, text_color, changeWhat=None, changeColor=None):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self.changeWhat = changeWhat
        self.changeColor = changeColor

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.length, self.height)

    def create_button(self):
        surface = self.draw_button()
        surface = self.write_text()

    def write_text(self):
        font_size = int(self.length // len(self.text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(self.text, 1, self.text_color)
        self.surface.blit(myText, ((self.x + self.length / 2) - myText.get_width() / 2, (self.y + self.height / 2) - myText.get_height() / 2))
        return self.surface

    def draw_button(self):
        for i in range(1, 10):
            s = pygame.Surface((self.length + (i * 2), self.height + (i * 2)))
            s.fill(self.color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, self.color, (self.x - i, self.y - i, self.length + i, self.height + i), self.width)
            self.surface.blit(s, (self.x - i, self.y - i))
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.height), 0)
        pygame.draw.rect(self.surface, (190, 190, 190), (self.x, self.y, self.length, self.height), 1)
        return self.surface