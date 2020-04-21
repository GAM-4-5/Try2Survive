from Loader import *
from Enemy import *
from Player import *

clock = pygame.time.Clock()
print(windowWidth, windowHeight)
player = Player(windowWidth / 2, windowHeight / 2)  # Igrač pozicioniran na sredinu prozora

explosionCount = 6  # Counter za iteraciju po listi slika eksplozije
explosionCoords = (0, 0)  # Koordinate na kojima se rpikazuje eksplozija

enemies = []  # Lista neprijatelja
maxEnemyNumber = 5  # Početni broj maksimalnog mogućeg broja neprijatelja koji se mogu instacirati i prikazati u prozoru

gameOver = False  # Kada je True igra završava
# Prikazuje neprijatelje u prozoru i provjerava je li igrač pogođen
def enemyCheck():
    global explosionCount, explosionCoords, gameOver
    if explosionCount < 6:
        window.blit(explosion[explosionCount], explosionCoords)  # Prikazuje određeni frame eksplozije
        explosionCount += 1

    # Prolazi kroz listu neprijatelja
    for enemy in enemies:
        # Briše neprijatelje koji su izašli iz vidljivog djela prozora
        if (enemy.x1 + enemy.width < 0 or enemy.x1 - enemy.width > windowWidth) or (
                enemy.y1 + enemy.height < 0 or enemy.y1 - enemy.height > windowHeight):
            enemies.pop(enemies.index(enemy))

        # Provjerava je li igrač pogođen te ovisno o tome briše neprijatelja i povećava njegov hitCount
        if player.isHit(enemy):
            gameOver = player.health <= 0
            playerHitSoundEffect.play(0)
            explosionCount = 0
            # Postavlja koordinate eksplozije na mjesto gdje se preklapaju hitbox od igrača i hitbox od neprijatelja
            explosionCoords = (player.hitbox.clip(enemy.hitbox).topleft[0] - 32,
                               player.hitbox.clip(enemy.hitbox).topleft[1] - 32)
            enemies.pop(enemies.index(enemy))
        else:
            player.score += 0.01

        enemy.draw(window)  # Prikazuje neprijatelja
        enemy.move()  # Pomiče neprijatelja

playerImage = pygame.transform.scale(pygame.image.load('Assets/player.png'), (60, 60))
# Prikazuje health bar i score igrača u prozoru
def drawGameStatusInfo():
    damageBar = pygame.Rect(windowWidth // 2 - 300, 30, 600, 25)
    healthBar = pygame.Rect(windowWidth // 2 - 300, 30, 1.2 * player.health, 25)
    pygame.draw.rect(window, red, damageBar)
    pygame.draw.rect(window, (0, 180, 0), healthBar)
    window.blit(playerImage, (healthBar.midright[0] - playerImage.get_width() // 2, healthBar.centery - playerImage.get_height() // 2))
    healthText = font.render(str(round(player.health / 5, 1)) + "%", 100, white)
    window.blit(healthText, (damageBar.centerx - healthText.get_width() // 2, damageBar.centery - healthText.get_height() // 2))

    text = font.render("Score: " + str(round(player.score, 0)), 100, white)
    window.blit(text, (windowWidth - text.get_width() - 50, 20))

i = 0
# Prikazuje pygame prozor i objekte u njemu
def redrawWindow():
    global i
    window.blit(backgroundImages[int(i//1)], (0, 0))  # Postavlja pozadinu prozora
    i = (i + 0.5) % 202

    player.draw(window)  # Prikazuje igrača u prozoru
    enemyCheck()
    drawGameStatusInfo()
    pygame.display.update()  # Ažurira prozor kako bi se vidjele napravljene promjene

# ------------------------ MAIN PETLJA ------------------------ #
pygame.time.delay(200)
pygame.mixer.music.play(-1)
run = True  # Uvjet za izvršavanje petlje
while run:
    clock.tick(framerate)  # Postavlja framerate igre

    # Petlja koja prolazi kroz evente koje generira korisnik
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Provjerava je li korisnik klikuo na X za izlaz iz igre
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
    if len(enemies) < maxEnemyNumber:
        enemy = Enemy()
        enemies.append(enemy)
        # Povećava maksimalan broj neprijatelja do 30
        if maxEnemyNumber < 20:
            maxEnemyNumber *= 1.01

    redrawWindow()

    #TODO: napraviti game over izbornik
    if gameOver:
        pygame.mixer.music.stop()
        gameOverSoundEffect.play(0)
        k = 10
        delay = int(gameOverSoundEffect.get_length() * 1000 // k) - 50
        for i in range(0, k + 1):
            pygame.time.delay(delay)
            rect = pygame.Rect(0, 0, windowWidth, (i + 1) * windowHeight // k)
            pygame.draw.rect(window, black, rect)
            pygame.display.update()
        break

pygame.quit()
