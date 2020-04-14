from Player import *

pygame.init()
window = pygame.display.set_mode((1500, 750)) #Definira pygame prozor i njegove dimenzije
pygame.display.set_caption("Try2Survive") #Postavlja naslov pygame prozora
player = Player(50, 50, 64, 64)
backgroundImage = pygame.image.load('background.jpg')

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

def redrawWindow():
    window.blit(backgroundImage, (0, 0))
    player.draw(window)
    pygame.display.update() #Ažurira prozor kako bi vidjeli napravljene promjene

#main
run = True #Uvjet za izvršavanje petlje
while run:
    pygame.time.delay(30)
    for event in pygame.event.get(): #Petlja koja prolazi kroz evente - interakcija korisnika i igre
        if event.type == pygame.QUIT:
            run = False

    movePlayer()
    redrawWindow()

pygame.quit()