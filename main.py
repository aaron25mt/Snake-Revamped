import pygame, sys, os, random, snake, food
from pygame.locals import *

class Game(object):
    def __init__(self, name="Snake Revamped", size=(640, 480)):
        self.name = name
        self.size = size
        self.colors = {'red': pygame.Color(255, 0, 0), 'blue': pygame.Color(0, 0, 255), 'green': pygame.Color(0, 255, 0), 'white': pygame.Color(255, 255, 255), 'black': pygame.Color(0, 0, 0)}
        self.settings = {'backgroundImg': self.colors['white'], 'snakeHead': self.colors['red'],'snakeBody': self.colors['blue'], 'snakeFood': self.colors['green']}

    def main(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)
        backgroundImgSettings, snakeHeadSettings, snakeBodySettings, snakeFoodSettings = self.showMainMenu()

        self.window.fill(self.settings['backgroundImg'])

        pygame.draw.rect(self.window, self.colors['white'], [545, 5, 100, 40])
        self.font = pygame.font.Font(None, 40)

        self.fpsClock = pygame.time.Clock()
        self.snake = snake.SnakeHead((320, 240), self.settings['snakeHead'], self.window)
        self.food = food.Food(self.settings['snakeFood'], self.window)
        self.food.drawFood()
        self.playGame()

    def showGameOver(self):
        while True:
            for event in pygame.event.get():
                if(event.type == QUIT):
                    self.quitGame()
                elif(event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                    self.main()
            self.font = pygame.font.Font(None, 80)
            self.window.fill(self.settings['backgroundImg'])
            self.window.blit(self.font.render("GAME OVER", False, self.colors['black']), (100, 145))
            self.window.blit(self.font.render("Final Score: " + str(self.snake.length), True, self.colors['black']), (95, 215))
            self.font = pygame.font.Font(None, 45)
            self.window.blit(self.font.render("Press <ENTER> to Restart", False, self.colors['black']), (85, 285))
            pygame.draw.line(self.window, self.colors['black'], (10, 10), (535, 10))
            pygame.draw.line(self.window, self.colors['black'], (10, 470), (535, 470))
            pygame.draw.line(self.window, self.colors['black'], (10, 0), (10, 480))
            pygame.draw.line(self.window, self.colors['black'], (535, 0), (535, 480))
            pygame.display.update()

    def showMainMenu(self):
        return "hello", "what" ,"are", "you"
        pass
        #if play game:
        #playgame()
        #else if options:
        #showoptions()
        #else if exit:
        #quitGame()
        #return backgroundImgSettings, snakeHeadSettings, snakeBodySettings, snakeFoodSettings

    def playGame(self):
        while not self.snake.dead:
            for event in pygame.event.get():
                if(event.type == QUIT):
                    self.quitGame()
            self.window.fill(self.settings['backgroundImg'])
            self.snake.updatePosition()
            self.food.drawFood()
            xLoc = 610 if (self.snake.length < 10) else 600 if (self.snake.length < 100) else 580 if (self.snake.length < 1000) else 565
            self.window.fill(self.settings['backgroundImg'], (xLoc, 35, 100, 35))
            self.window.blit(self.font.render("Score:", False, self.colors['black']), (545, 5))
            self.window.blit(self.font.render(str(self.snake.length), True, self.colors['black']), (xLoc, 35))
            pygame.draw.line(self.window, self.colors['black'], (10, 10), (535, 10))
            pygame.draw.line(self.window, self.colors['black'], (10, 470), (535, 470))
            pygame.draw.line(self.window, self.colors['black'], (10, 0), (10, 480))
            pygame.draw.line(self.window, self.colors['black'], (535, 0), (535, 480))
            pygame.display.update()
        self.showGameOver()

    def collisionTest(self, x1, x2, y1, y2, w1, w2, h1, h2):
        return x1 + w1 > x2 and x2 + w2 > x1 and y1 + h1 > y2 and y2 + h2 > y1

    def quitGame(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.main()