import pygame, random

class FoodPiece(object):
    def __init__(self, color, window):
        '''initiate a food piece'''
        self.color = color
        self.window = window
        loc = self.getRandomLocation() #random location for each piece
        self.xPos = loc[0]
        self.yPos = loc[1]

    def getRect(self):
        '''returns the rect of the food'''
        return pygame.Rect(self.xPos, self.yPos, 15, 15)

    def drawFood(self):
        '''draw the food piece'''
        pygame.draw.rect(self.window, self.color, pygame.Rect(self.xPos, self.yPos, 15, 15))

    def getRandomLocation(self):
        '''get a random in-bounds location'''
        return [random.randint(15, 515), random.randint(15, 450)]

class Food(object):
    def __init__(self, snake, color, window):
        '''initiate food'''
        self.snake = snake
        self.color = color
        self.window = window
        self.foods = []

    def updateFood(self, snake):
        '''updates and checks the food'''
        if(len(self.foods) <= 0): #if there's no food on screen
            food = FoodPiece(self.color, self.window) #create a new food piece
            self.foods.append(food) #so we know a piece exists
        for piece in self.foods:
            #if(0 <= abs(piece.xPos - snake.xPos) <= 15 and 0 <= abs(piece.yPos - snake.yPos) <= 15): #if the snake head is relatively close to the food
            if(snake.getRect().colliderect(piece.getRect())):
                snake.length += 1 #make the snake bigger
                self.foods.remove(piece) #remove the food piece
            piece.drawFood() #draw the food