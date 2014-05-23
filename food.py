import pygame, random

class FoodPiece(object):
    def __init__(self, color, window):
        self.color = color
        self.window = window
        self.drawFood(window)

    def drawFood(self, window):
        loc = list(self.getRandomLocation())
        self.xPos = loc[0]
        self.yPos = loc[1]
        pygame.draw.rect(window, self.color, pygame.Rect(self.xPos, self.yPos, 15, 15))

    def getRandomLocation(self):
        return (random.randint(15, 530), random.randint(15, 465))

class Food(object):
    def __init__(self, color, window):
        self.color = color
        self.window = window
        self.foods = []
        self.drawFood()

    def drawFood(self):
        if(len(self.foods) != 1):
            food = FoodPiece(self.color, self.window)
            self.foods.append(food)

    def updateFood(self):
        pass