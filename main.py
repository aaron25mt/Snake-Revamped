import pygame, sys, os, random, snake, food
from pygame.locals import *

class Game(object):
    '''initiate a game'''
    def __init__(self, name="Snake Revamped", size=(640, 480)):
        self.name = name
        self.size = size
        self.colors = {'red': pygame.Color(255, 0, 0), 'blue': pygame.Color(0, 0, 255), 'green': pygame.Color(0, 255, 0), 'white': pygame.Color(255, 255, 255), 'black': pygame.Color(0, 0, 0)}
        self.settings = {'backgroundImg': self.colors['green'], 'snakeColor': self.colors['blue'], 'snakeFood': self.colors['white']}

    def main(self):
        '''start a game'''
        pygame.init()
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)

        self.window.fill(self.settings['backgroundImg'])

        #pygame.draw.rect(self.window, self.colors['white'], [545, 5, 100, 40])
        self.font = pygame.font.Font(None, 40)

        self.fpsClock = pygame.time.Clock()
        self.snake = snake.SnakeHead((272.5, 240), self.settings['snakeColor'], self.window) #create the snake head
        self.food = food.Food(self.snake, self.settings['snakeFood'], self.window) #create the food
        self.playGame()

    def showGameOver(self):
        '''show the game over screen'''
        while True:
            for event in pygame.event.get():
                if(event.type == QUIT):
                    self.quitGame()
                elif(event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                    self.main() #allows players to restart the game. to mr. hyman: hint ;)
            self.font = pygame.font.Font(None, 80)
            self.window.fill(self.settings['backgroundImg']) #get rid of everything on the screen
            self.window.blit(self.font.render("GAME OVER", False, self.colors['black']), (100, 145))
            self.window.blit(self.font.render("Final Score: " + str(self.snake.length-1), True, self.colors['black']), (80, 215)) #score is how many foods eaten aka length - 1
            self.font = pygame.font.Font(None, 45)
            self.window.blit(self.font.render("Press <ENTER> to Restart", False, self.colors['black']), (85, 285))
            self.drawBounds()
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
        '''start the game from the beginning'''
        while not self.snake.dead:
            for event in pygame.event.get():
                if(event.type == QUIT):
                    self.quitGame()
            self.window.fill(self.settings['backgroundImg'])
            self.snake.updatePosition()
            self.food.updateFood(self.snake)
            xLoc = 610 if (self.snake.length < 10) else 600 if (self.snake.length < 100) else 580 if (self.snake.length < 1000) else 565 #account for the number of digits
            self.window.fill(self.settings['backgroundImg'], (xLoc, 35, 100, 35))
            self.window.blit(self.font.render("Score:", False, self.colors['black']), (545, 5))
            self.window.blit(self.font.render(str(self.snake.length-1), True, self.colors['black']), (xLoc, 35))
            self.drawBounds()
            pygame.display.update()
        self.showGameOver()

    def drawBounds(self): #since we do this twice
        '''draws the bounding lines'''
        pygame.draw.line(self.window, self.colors['black'], (10, 10), (535, 10))
        pygame.draw.line(self.window, self.colors['black'], (10, 470), (535, 470))
        pygame.draw.line(self.window, self.colors['black'], (10, 0), (10, 480))
        pygame.draw.line(self.window, self.colors['black'], (535, 0), (535, 480))

    def quitGame(self):
        '''exits the game'''
        pygame.quit()
        sys.exit()

if __name__ == "__main__": #i have no idea how/why this works
    game = Game()
    game.main()