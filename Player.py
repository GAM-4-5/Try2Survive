import pygame
from Config import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.speed = 10
        self.image = pygame.image.load('player.png') # Import slike igrača
        self.angle = 0

    # Crta igrača u prozoru
    def draw(self, window):
        image = pygame.transform.rotate(self.image, self.angle) # Rotira sliku igrača
        window.blit(image, (self.x - int(image.get_width() / 2), self.y - int(image.get_height() / 2))) # Centrira rotiranu sliku
        self.angle = (self.angle + 7) % 360

    # Pomiče igrača do gornjeg ruba prozora
    def moveUp(self):
        if (self.y - self.height / 2 - 10) > 0:
            self.y -= self.speed

    # Pomiče igrača do donjeg ruba prozora
    def moveDown(self):
        if (self.y + self.height / 2 + 10) < windowHeight:
            self.y += self.speed

    # Pomiče igrača do desnog ruba prozora
    def moveRight(self):
        if (self.x + self.width / 2 + 10) < windowWidth:
            self.x += self.speed

    # Pomiče igrača do lijevog ruba prozora
    def moveLeft(self):
        if (self.x - self.width / 2 - 10) > 0:
            self.x -= self.speed

    # Vraća osnovne vrijednosti instance Player
    def values(self):
        return self.x, self.y, self.width, self.height

