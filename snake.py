import pygame

class SnakeBody(object):
    def __init__(self, xPos, yPos, color, window):
        self.xPos = xPos
        self.yPos = yPos
        self.color = color
        self.drawBody(window)

    def drawBody(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.xPos, self.yPos, 15, 15))

class SnakeHead(object):
    def __init__(self, XYpos, color, window):
        self.xPos = list(XYpos)[0]
        self.yPos = list(XYpos)[1]
        self.temp_x = 0
        self.temp_y = 0
        self.color = color
        self.window = window
        self.length = 0
        self.dead = False

        self.time_elapsed = 0
        self.fpsClock = pygame.time.Clock()

        self.tail = []
        self.head = SnakeBody(self.xPos, self.yPos, color, window)
        self.direction = 0

    def updatePosition(self):
        dt = self.fpsClock.tick(15)
        self.time_elapsed += dt
        keyPressed = pygame.key.get_pressed()
        if(keyPressed[pygame.K_UP]):
            self.direction = 0
            self.temp_x, self.temp_y = 0, -15
        elif(keyPressed[pygame.K_RIGHT]):
            self.direction = 1
            self.temp_x, self.temp_y = 15, 0
        elif(keyPressed[pygame.K_DOWN]):
            self.direction = 2
            self.temp_x, self.temp_y = 0, 15
        elif(keyPressed[pygame.K_LEFT]):
            self.direction = 3
            self.temp_x, self.temp_y = -15, 0
        if(self.time_elapsed > 50):
            self.tail.insert(0, SnakeBody(self.xPos, self.yPos, self.color, self.window))
            self.xPos += self.temp_x
            self.yPos += self.temp_y
            if(len(self.tail) > self.length):
                self.tail.pop(len(self.tail)-1)
            self.blitScreen(self.window)
            self.time_elapsed = 0
        self.checkIfDead()

    def eatFood(self):
        self.length += 1

    def blitScreen(self, window):
        for t in self.tail:
            t.drawBody(window)
        self.head

    def checkIfDead(self):
        for rect in self.tail:
            if(rect.xPos == self.xPos and rect.yPos == self.yPos):
                self.dead = True
        if(self.xPos < 10 or self.yPos < 10 or self.xPos > 535 or self.yPos > 470):
            self.dead = True