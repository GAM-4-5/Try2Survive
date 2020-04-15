import pygame
from random import randint
from Config import *


class Enemy:
    def __init__(self):
        self.x = randint(0, 3)  # Generira random broj o kojem ovisi smjer iz kojeg dolazi neprijatelj
        # Neprijatelj dolazi s lijeve strane
        if self.x == 0:
            self.x1 = -32
            self.y1 = randint(0, windowHeight)
            self.x2 = windowWidth + 32
            self.y2 = randint(0, windowHeight)
        # Neprijatelj dolazi s gornje strane
        elif self.x == 1:
            self.x1 = randint(0, windowWidth)
            self.y1 = -32
            self.x2 = randint(0, windowWidth)
            self.y2 = windowHeight + 32
        # Neprijatelj dolazi s desne strane
        elif self.x == 2:
            self.x1 = windowWidth + 32
            self.y1 = randint(0, windowHeight)
            self.x2 = -32
            self.y2 = randint(0, windowHeight)
        # Neprijatelj dolazi s donje strane
        else:
            self.x1 = randint(0, windowWidth)
            self.y1 = windowHeight + 32
            self.x2 = randint(0, windowWidth)
            self.y2 = -32
        # Pomak objekta po x i y osi u jednom frameu
        self.dx = (self.x2 - self.x1) / framerate
        self.dy = (self.y2 - self.y1) / framerate

        self.width = 32
        self.height = 32
        self.speedFactor = randint(3, 6)
        self.image = pygame.image.load('Assets/enemy.png')  # Import slike neprijatelja
        self.imageAngle = 0
        self.hitbox = pygame.Rect(self.x1 - self.width / 2, self.y1 - self.height / 2, self.width, self.height)

    # Vraća koordinate neprijatelja
    def getCoordinates(self):
        return self.x1, self.y1

    # Vraća centralne koordinate neprijatelja
    def getCenterCoordinates(self):
        return self.x1 + self.width / 2, self.y1 + self.height / 2

    # Crta neprijatelja u prozoru
    def draw(self, window):
        image = pygame.transform.rotate(self.image, self.imageAngle)  # Rotira sliku neprijatelja
        window.blit(image, (
        self.x1 - int(image.get_width() / 2), self.y1 - int(image.get_height() / 2)))  # Centrira rotiranu sliku
        self.imageAngle = (self.imageAngle + 3) % 360
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        self.hitbox = pygame.Rect(self.x1 - self.width / 2, self.y1 - self.height / 2, self.width, self.height)

    # Pomiče neprijatelja preko prozora po zadaoj putanji
    def move(self):
        if (0 < self.x1 + self.width and self.x1 < windowWidth) or (
                0 < self.y1 + self.height and self.y1 < windowHeight):
            self.x1 += self.dx / self.speedFactor
            self.y1 += self.dy / self.speedFactor
