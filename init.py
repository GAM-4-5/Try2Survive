import pygame
from Config import *
from Enemy import *
from Player import *

pygame.init() # Početna inicijaliaicija pygame modula

window = pygame.display.set_mode((windowWidth, windowHeight)) # Definira pygame prozor i njegove dimenzije
pygame.display.set_caption("Try2Survive") # Postavlja naslov pygame prozora
clock = pygame.time.Clock()

backgroundImage = pygame.image.load('Assets/background.jpg') # Import pozadine
backgroundImageAngle = 0

# Import slika eksplozije
explosion = [pygame.image.load('Assets/explosion/explosion1.png'), pygame.image.load('Assets/explosion/explosion2.png'),
             pygame.image.load('Assets/explosion/explosion3.png'), pygame.image.load('Assets/explosion/explosion4.png'),
             pygame.image.load('Assets/explosion/explosion5.png'), pygame.image.load('Assets/explosion/explosion6.png')]
explosionCount = 6
explosionCoords = (0, 0)

player = Player(windowWidth / 2, windowHeight / 2) # Igrač
enemies = [] # Lista neprijatelja

# Prikazuje pygame prozor i objekte u njemu
def redrawWindow():
    window.blit(backgroundImage, (0, 0)) # Postavlja pozadinu prozora
    player.draw(window) # Prikazuje igrača u prozoru

    global explosionCount, explosionCoords
    if explosionCount < 6:
        window.blit(explosion[explosionCount], explosionCoords) # Prikazuje određeni frame eksplozije
        explosionCount += 1

    # Prolazi kroz listu neprijatelja
    for enemy in enemies:

        # Briše neprijatelje koji su izašli iz vidljivog djela prozora
        if (enemy.x1 + enemy.width < 0 or enemy.x1 - enemy.width > windowWidth) or (enemy.y1 + enemy.height < 0 or enemy.y1 - enemy.height > windowHeight):
            enemies.pop(enemies.index(enemy))

        #Provjerava je li igrač pogođen te ovisno o tome briše neprijatelja i povećava njegov hitCount
        if player.isHit(enemy):
            player.hitCount += 1
            explosionCount = 0
            explosionCoords = (player.hitbox.clip(enemy.hitbox).topleft[0] - 32, player.hitbox.clip(enemy.hitbox).topleft[1] - 32)
            enemies.pop(enemies.index(enemy))

        enemy.draw(window) # Prikazuje neprijatelja
        enemy.move() # Pomiče neprijatelja

    pygame.display.update() # Ažurira prozor kako bi se vidjele napravljene promjene


# ------------------------ MAIN PETLJA ------------------------ #
run = True # Uvjet za izvršavanje petlje
while run:
    clock.tick(framerate) # Postavlja framerate igre

    # Petlja koja prolazi kroz evente koje generira korisnik
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Provjerava je li korisnik klikuo na X za izlaz iz igre
            run = False

    # Poziva određene funkcije ovisno o pritisnutoj tipki
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    if keys[pygame.K_UP]:
        player.moveUp()
    if keys[pygame.K_DOWN]:
        player.moveDown()
    if keys[pygame.K_ESCAPE]:
        run = False

    # Stvara nove neprijatelje kada stari nestanu iz vidljivog područja prozora
    if len(enemies) < 15:
        enemy = Enemy()
        enemies.append(enemy)

    redrawWindow()

pygame.quit()