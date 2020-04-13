import pygame
import random
from Player import *

pygame.init()

window = pygame.display.set_mode((1500, 750)) #Definira pygame prozor i njegove dimenzije
pygame.display.set_caption("Try2Survive") #Postavlja naslov pygame prozora

x, y = 50, 50 #Početne koordinate igrača
width, height = 50, 50 #Dimenzije igrača
speed = 25 #Brzina igrača
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
player = Player(x, y, width, height, speed, color)

def movePlayer(): #Pomiče igrača ovisno o pritisnutoj tipki
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight(window.get_width())
    if keys[pygame.K_UP]:
        player.moveUp()
    if keys[pygame.K_DOWN]:
        player.moveDown(window.get_height())

def changePlayerColor():
    player.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

run = True #Uvjet za izvršavanje petlje
while run:
    pygame.time.delay(30)
    for event in pygame.event.get(): #Petlja koja prolazi kroz evente - interakcija korisnika i igre
        if event.type == pygame.QUIT:
            run = False

    movePlayer()
    changePlayerColor()

    window.fill((0, 0, 0))
    pygame.draw.rect(window, player.color, player.values()) #Prikazuje igrača u prozoru
    pygame.display.update() #Ažurira prozor kako bi vidjeli napravljene promjene

pygame.quit()