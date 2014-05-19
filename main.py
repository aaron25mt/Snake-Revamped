import pygame, sys, os
from pygame.locals import *

def setup():
    pygame.init()
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Snake Revamped")
    colors = {'red': pygame.Color(255, 0, 0), 'blue': pygame.Color(0, 0, 255), 'green': pygame.Color(0, 255, 0), 'white': pygame.Color(255, 255, 255), 'black': pygame.Color(0, 0, 0)}
    settings = {'backgroundImg': 'default.png'}
    startGame()

def startGame():
    while True:
        pygame.display.update()

if __name__ == "__main__":
    setup()