import pygame

class SnakeBody(object):
    def __init__(self, xPos, yPos, color, window):
        '''initiate and draw a snake part'''
        self.xPos = xPos
        self.yPos = yPos
        self.color = color
        self.drawBody(window) #when created, draw the box

    def drawBody(self, window):
        '''draw the snake part to the screen'''
        pygame.draw.rect(window, self.color, pygame.Rect(self.xPos, self.yPos, 15, 15)) #15, 15 is the size of the box

class SnakeHead(object):
    def __init__(self, XYpos, color, window):
        '''initiate the snake'''
        #list(XYpos)[x] allows us to enter XYpos as a tuple!
        self.xPos = list(XYpos)[0]
        self.yPos = list(XYpos)[1]
        self.temp_x = 0
        self.temp_y = 0
        self.color = color
        self.window = window
        self.length = 1
        self.dead = False

        self.time_elapsed = 0
        self.fpsClock = pygame.time.Clock()

        self.tail = []
        self.head = SnakeBody(self.xPos, self.yPos, color, window)
        self.direction = -1
        # direction number corresponds to up, right, down, and left. see line #37

    def updatePosition(self):
        '''update the snakes position'''
        dt = self.fpsClock.tick(15) #prevents snake from 'blinking'
        self.time_elapsed += dt
        keyPressed = pygame.key.get_pressed()
        if(keyPressed[pygame.K_UP] and self.direction != 2): #so head doesn't go into the tail. same for lines #40, 43, & 46
            self.direction = 0
            self.temp_x, self.temp_y = 0, -15 #changes the box location based on size (15 * 15). same for lines #42, 45, 48
        elif(keyPressed[pygame.K_RIGHT] and self.direction != 3):
            self.direction = 1
            self.temp_x, self.temp_y = 15, 0
        elif(keyPressed[pygame.K_DOWN] and self.direction != 0):
            self.direction = 2
            self.temp_x, self.temp_y = 0, 15
        elif(keyPressed[pygame.K_LEFT] and self.direction != 1):
            self.direction = 3
            self.temp_x, self.temp_y = -15, 0
        if(self.time_elapsed > 50): #do this check pretty fast and often (.05 seconds)
            self.tail.insert(0, SnakeBody(self.xPos, self.yPos, self.color, self.window)) #add the current head to the front of the tail
            self.xPos += self.temp_x
            self.yPos += self.temp_y
            self.blitScreen(self.window) #draw the 'new snake'
            if(len(self.tail) > self.length-1):
                self.tail.pop(len(self.tail)-1) #remove the old tail
            self.time_elapsed = 0 #reset
        self.checkIfDead() #make sure the game's not over

    def blitScreen(self, window):
        '''draw the entire snake to the screen'''
        for t in self.tail:
            t.drawBody(window)
        self.head

    def checkIfDead(self):
        '''make sure the snake is in bounds and not eating itself'''
        for rect in self.tail:
            if(rect.xPos == self.xPos and rect.yPos == self.yPos):
                self.dead = True
        if(self.xPos < 15 or self.yPos < 15 or self.xPos > 525 or self.yPos > 465):
            self.dead = True