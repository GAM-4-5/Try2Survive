import pygame

playerImage = pygame.image.load('player.png')

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 25

    def draw(self, window):
        window.blit(playerImage, (self.x, self.y))

    def moveUp(self):
        if self.y > 0: #Pomiče igrača do gornjeg ruba prozora
            self.y -= self.speed

    def moveDown(self, windowHeight):
        if self.y < (windowHeight - self.height): #Pomiče igrača do donjeg ruba prozora
            self.y += self.speed

    def moveRight(self, windowWidth):
        if self.x < (windowWidth - self.width): #Pomiče igrača do desnog ruba prozora
            self.x += self.speed

    def moveLeft(self):
        if self.x > 0: #Pomiče igrača do lijevog ruba prozora
            self.x -= self.speed

    def values(self):
        return (self.x, self.y, self.width, self.height)

