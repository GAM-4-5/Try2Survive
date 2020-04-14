from Config import *
from Enemy import *
from Player import *

pygame.init() # Početna inicijaliaicija pygame modula

window = pygame.display.set_mode((windowWidth, windowHeight)) # Definira pygame prozor i njegove dimenzije
pygame.display.set_caption("Try2Survive") # Postavlja naslov pygame prozora
clock = pygame.time.Clock()

backgroundImage = pygame.image.load('background.jpg') # Import pozadine

player = Player(50, 50) # Igrač
enemies = [] # Lista neprijtelja

# Crta pygame prozor i objekte u njemu
def redrawWindow():
    window.blit(backgroundImage, (0, 0))
    player.draw(window)

    # Prolazi kroz listu neprijatelja te briše neprijatelje koji su izašli iz vidljivog područja prozora
    for enemy in enemies:
        if (enemy.x1 + enemy.width < 0 or enemy.x1 - enemy.width > windowWidth) or (enemy.y1 + enemy.height < 0 or enemy.y1 - enemy.height > windowHeight):
            enemies.pop(enemies.index(enemy))
        enemy.draw(window)
        enemy.move()

    pygame.display.update() # Ažurira prozor kako bi se vidjele napravljene promjene

# main
run = True # Uvjet za izvršavanje petlje
while run:
    clock.tick(framerate) # Postavlja framerate igre

    # Petlja koja prolazi kroz evente koje generira korisnik
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    if len(enemies) < 10:
        enemy = Enemy()
        enemies.append(enemy)

    redrawWindow()

pygame.quit()