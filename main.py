import pygame, sys, os, random, snake, food, button
from pygame.locals import *

class Game(object):
    '''initiate a game'''
    def __init__(self, name="Snake Revamped", size=(640, 480), hiscore=0):
        self.name = name
        self.size = size
        if(hiscore == None):
            self.hiscore = 0
        else:
            self.hiscore = self.getHighScore()
        self.colors = {'red': pygame.Color(255, 0, 0), 'blue': pygame.Color(0, 0, 255), 'green': pygame.Color(0, 255, 0), 'white': pygame.Color(255, 255, 255), 'black': pygame.Color(0, 0, 0)}
        self.settings = {'backgroundColor': self.colors['white'], 'snakeColor': self.colors['red'], 'snakeFood': self.colors['green']}
        pygame.init()
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)
        self.showMainMenu()

    def main(self):
        '''start a game'''
        self.window.fill(self.settings['backgroundColor'])
        self.font = pygame.font.Font(None, 40)
        self.fpsClock = pygame.time.Clock()
        self.snake = snake.SnakeHead((272.5, 240), self.settings['snakeColor'], self.window) #create the snake head
        self.food = food.Food(self.snake, self.settings['snakeFood'], self.window) #create the food
        self.playGame()

    def showGameOver(self):
        '''show the game over screen'''
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.quitGame()
                elif(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_RETURN):
                        self.main()
                    elif(event.key == pygame.K_ESCAPE):
                        self.showMainMenu()
            self.font = pygame.font.Font(None, 80)
            self.window.fill(self.settings['backgroundColor']) #get rid of everything on the screen
            if(self.settings['backgroundColor'] != self.colors['black']):
                self.window.blit(self.font.render("GAME OVER", False, self.colors['black']), (100, 145))
                self.window.blit(self.font.render("Final Score: " + str(self.snake.length-1), True, self.colors['black']), (80, 215)) #score is how many foods eaten aka length - 1
            else:
                self.window.blit(self.font.render("GAME OVER", False, self.colors['white']), (100, 145))
                self.window.blit(self.font.render("Final Score: " + str(self.snake.length-1), True, self.colors['white']), (80, 215)) #score is how many foods eaten aka length - 1
            self.font = pygame.font.Font(None, 25)
            if(self.settings['backgroundColor'] != self.colors['black']):
                self.window.blit(self.font.render("Press <ENTER> to Restart, Press <ESCAPE> for Main Menu", False, self.colors['black']), (35, 285))
            else:
                self.window.blit(self.font.render("Press <ENTER> to Restart, Press <ESCAPE> for Main Menu", False, self.colors['white']), (35, 285))
            self.drawBounds()
            pygame.display.update()

    def showOptionsMenu(self):
        '''shows the option menu'''
        buttons = []
        bg = pygame.image.load("bg.jpg").convert()
        self.window.blit(bg, [0, 0])
        optionsFont = pygame.font.Font(None, 32)
        pygame.draw.rect(self.window, self.colors['white'], (35, 10, 130, 50))
        self.window.blit(optionsFont.render("Background", 1, self.colors['red']), (35, 10))
        self.window.blit(optionsFont.render("Color", 1, self.colors['red']), (70, 35))
        backgroundwhitebutton = button.Button(self.window, self.colors['black'],50, 70, 100, 50, 50, 'White', self.colors['white'], "backgroundColor", "white")
        backgroundredbutton = button.Button(self.window, self.colors['black'],50, 140, 100, 50, 50, ' Red ', self.colors['white'], "backgroundColor", "red")
        backgroundgreenbutton = button.Button(self.window, self.colors['black'],50, 210, 100, 50, 50, 'Green', self.colors['white'], "backgroundColor", "green")
        backgroundbluebutton = button.Button(self.window, self.colors['black'],50, 280, 100, 50, 50, ' Blue', self.colors['white'], "backgroundColor", "blue")
        backgroundblackbutton = button.Button(self.window, self.colors['black'],50, 350, 100, 50, 50, 'Black', self.colors['white'], "backgroundColor", "black")
        pygame.draw.rect(self.window, self.colors['white'], (285, 10, 70, 50))
        self.window.blit(optionsFont.render("Snake", 1, self.colors['red']), (285, 10))
        self.window.blit(optionsFont.render("Color", 1, self.colors['red']), (290, 35))
        snakewhitebutton = button.Button(self.window, self.colors['black'],270, 70, 100, 50, 50, 'White', self.colors['white'], "snakeColor", "white")
        snakeredbutton = button.Button(self.window, self.colors['black'],270, 140, 100, 50, 50, ' Red ', self.colors['white'], "snakeColor", "red")
        snakegreenbutton = button.Button(self.window, self.colors['black'],270, 210, 100, 50, 50, 'Green', self.colors['white'], "snakeColor", "green")
        snakebluebutton = button.Button(self.window, self.colors['black'],270, 280, 100, 50, 50, ' Blue', self.colors['white'], "snakeColor", "blue")
        snakeblackbutton = button.Button(self.window, self.colors['black'],270, 350, 100, 50, 50, 'Black', self.colors['white'], "snakeColor", "black")
        pygame.draw.rect(self.window, self.colors['white'], (510, 10, 60, 50))
        self.window.blit(optionsFont.render("Food", 1, self.colors['red']), (514, 10))
        self.window.blit(optionsFont.render("Color", 1, self.colors['red']), (510, 35))
        foodwhitebutton = button.Button(self.window, self.colors['black'],490, 70, 100, 50, 50, 'White', self.colors['white'], "snakeFood", "white")
        foodredbutton = button.Button(self.window, self.colors['black'],490, 140, 100, 50, 50, ' Red ', self.colors['white'], "snakeFood", "red")
        foodgreenbutton = button.Button(self.window, self.colors['black'],490, 210, 100, 50, 50, 'Green', self.colors['white'], "snakeFood", "green")
        foodbluebutton = button.Button(self.window, self.colors['black'],490, 280, 100, 50, 50, ' Blue', self.colors['white'], "snakeFood", "blue")
        foodblackbutton = button.Button(self.window, self.colors['black'],490, 350, 100, 50, 50, 'Black', self.colors['white'], "snakeFood", "black")
        donebutton = button.Button(self.window, self.colors['black'], 45, 415, 555, 50, 60, '     Done     ', self.colors['white'])
        buttons.extend([backgroundwhitebutton, backgroundredbutton, backgroundgreenbutton, backgroundbluebutton, backgroundblackbutton, snakewhitebutton, snakeredbutton, snakegreenbutton, snakebluebutton, snakeblackbutton, foodwhitebutton, foodredbutton, foodgreenbutton, foodbluebutton, foodblackbutton, donebutton])
        for x in buttons:
            x.create_button()
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.quitGame()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    mousePos = pygame.mouse.get_pos()
                    '''collidepoint checks if the mouse was clicked on the button'''
                    for x in buttons:
                        if(x.getRect().collidepoint(mousePos)):
                            if(x != donebutton):
                                self.settings[x.changeWhat] = self.colors[x.changeColor]
                            else:
                                self.showMainMenu()
            pygame.display.update()

    def showMainMenu(self):
        '''shows the main menu'''
        fullscreen = False
        while True:
            bg = pygame.image.load("bg.jpg").convert()
            self.window.blit(bg, [0, 0])
            logo = pygame.image.load("logo.jpg").convert()
            self.window.blit(logo, [(self.window.get_width()/2) - 96, 10])
            playgamebutton = button.Button(self.window, self.colors['black'], (self.window.get_width()/2)-50, 200, 100, 45, 50, ' Play ', self.colors['white'])
            optionsbutton = button.Button(self.window, self.colors['black'], (self.window.get_width()/2)-50, 265, 100, 45, 50, 'Options', self.colors['white'])
            fullsnbutton = button.Button(self.window, self.colors['black'], (self.window.get_width()/2)-50, 330, 100, 45, 50, 'Expand', self.colors['white'])
            exitbutton = button.Button(self.window, self.colors['black'], (self.window.get_width()/2)-50, 395, 100, 45, 50, ' Exit ', self.colors['white'])
            for x in [playgamebutton, optionsbutton, fullsnbutton, exitbutton]:
                x.create_button()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.quitGame()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    mousePos = pygame.mouse.get_pos()
                    '''collidepoint checks if the mouse was clicked on the button'''
                    if(playgamebutton.getRect().collidepoint(mousePos)):
                        self.main()
                    if(optionsbutton.getRect().collidepoint(mousePos)):
                        self.showOptionsMenu()
                    if(fullsnbutton.getRect().collidepoint(mousePos)):
                        fullscreen = not fullscreen
                        if(fullscreen):
                            pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
                        else:
                            pygame.display.set_mode((640, 480))
                    if(exitbutton.getRect().collidepoint(mousePos)):
                        self.quitGame()
            pygame.display.update()

    def playGame(self):
        '''start the game from the beginning'''
        while not self.snake.dead:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.quitGame()
            self.window.fill(self.settings['backgroundColor'])
            self.snake.updatePosition()
            self.checkScore()
            xLoc = 610 if (self.snake.length < 10) else 600 if (self.snake.length < 100) else 580 if (self.snake.length < 1000) else 565 #account for the number of digits
            self.window.fill(self.settings['backgroundColor'], (xLoc, 35, 100, 35))
            if(self.settings['backgroundColor'] != self.colors['black']):
                self.window.blit(self.font.render("Score:", False, self.colors['black']), (545, 5))
                self.window.blit(self.font.render(str(self.snake.length-1), True, self.colors['black']), (xLoc, 35))
                self.window.blit(pygame.font.Font(None, 30).render("Hi-Score:", False, self.colors['black']), (545, 95))
                self.window.blit(self.font.render(str(self.hiscore), True, self.colors['black']), (xLoc, 125))
            else:
                self.window.blit(self.font.render("Score:", False, self.colors['white']), (545, 5))
                self.window.blit(self.font.render(str(self.snake.length-1), True, self.colors['white']), (xLoc, 35))
                self.window.blit(pygame.font.Font(None, 30).render("Hi-Score:", False, self.colors['white']), (545, 95))
                self.window.blit(self.font.render(str(self.hiscore), True, self.colors['white']), (xLoc, 125))
            self.drawBounds()
            pygame.display.update()
        self.showGameOver()

    def checkScore(self):
        '''checks the current and high score'''
        self.food.updateFood(self.snake)
        self.checkCollison(self.snake, self.food)
        if(self.snake.length-1 > self.hiscore):
            self.hiscore = self.snake.length-1
            self.updateHighScore(self.snake.length-1, True)

    def checkCollison(self, snake, food):
        for piece in food.foods:
            if(snake.getRect().colliderect(piece.getRect())):
                snake.length += 1 #make the snake bigger
                food.foods.remove(piece) #remove the food piece
            piece.drawFood() #draw the food

    def getHighScore(self):
        '''reads and returns the current high score'''
        try:
            highscoreFile = open('highscore.txt', 'r')
            highscore = int(highscoreFile.read())
            highscoreFile.close()
            return highscore
        except IOError or ValueError:
            return 0

    def updateHighScore(self, newScore):
        '''updates the new highscore'''
        try:
            highscoreFile = open('highscore.txt', 'w')
            highscoreFile.write(str(newScore))
            highscoreFile.close()
        except IOError:
            print('Unable to record high score.')

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
    game = Game("Snake Rerevamped", (640, 480), 0)