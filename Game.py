from tkinter import *
from Loader import *
from Player import *
from Enemy import *

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.frameCounter = 0

        self.player = Player()  # Igrač
        self.playerImage = pygame.transform.scale(pygame.image.load('Assets/player.png'), (60, 60))

        self.explosionCount = 6  # Counter za iteraciju po listi slika eksplozije
        self.explosionCoords = (0, 0)  # Koordinate na kojima se rpikazuje eksplozija

        self.enemies = []  # Lista neprijatelja
        self.maxEnemyNumber = 5  # Početni broj maksimalnog mogućeg broja neprijatelja koji se mogu instacirati i prikazati u prozoru

        self.run = True  # Glavni uvjet za izvršavanje while petlje u main metodi
        self.isGameOver = False  # Kada je True igra završava
        self.isPlaying = False   # Boolean je li igra u tijeku ili ne

        self.backgroundImageIndex = 0

    # Prikazuje neprijatelje u prozoru i provjerava je li igrač pogođen
    def enemyCheck(self):
        if self.explosionCount < 6:
            window.blit(explosion[self.explosionCount], self.explosionCoords)  # Prikazuje određeni frame eksplozije
            self.explosionCount += 1

        # Prolazi kroz listu neprijatelja
        for enemy in self.enemies:
            # Briše neprijatelje koji su izašli iz vidljivog djela prozora
            if (enemy.x1 + enemy.width < 0 or enemy.x1 - enemy.width > windowWidth) or (
                    enemy.y1 + enemy.height < 0 or enemy.y1 - enemy.height > windowHeight):
                self.enemies.pop(self.enemies.index(enemy))

            # Provjerava je li igrač pogođen te ovisno o tome briše neprijatelja i povećava njegov hitCount
            if self.player.isHit(enemy):
                self.isGameOver = self.player.health <= 0
                playerHitSoundEffect.play(0)
                self.explosionCount = 0
                # Postavlja koordinate eksplozije na mjesto gdje se preklapaju hitbox od igrača i hitbox od neprijatelja
                self.explosionCoords = (self.player.hitbox.clip(enemy.hitbox).topleft[0] - 32,
                                   self.player.hitbox.clip(enemy.hitbox).topleft[1] - 32)
                self.enemies.pop(self.enemies.index(enemy))
            else:
                self.player.score += 0.01

            enemy.draw(window)  # Prikazuje neprijatelja
            enemy.move()  # Pomiče neprijatelja

    # Prikazuje health bar i score igrača u prozoru
    def drawGameStatusInfo(self):
        damageBar = pygame.Rect(int(windowWidth // 2 - 300), 30, 600, 25)
        healthBar = pygame.Rect(int(windowWidth // 2 - 300), 30, int(1.2 * self.player.health), 25)
        pygame.draw.rect(window, red, damageBar)
        pygame.draw.rect(window, (0, 180, 0), healthBar)
        window.blit(self.playerImage, (healthBar.midright[0] - self.playerImage.get_width() // 2,
                                       healthBar.centery - self.playerImage.get_height() // 2))
        healthText = font.render(str(round(self.player.health / 5, 1)) + "%", 100, white)
        window.blit(healthText,(damageBar.centerx - healthText.get_width() // 2,
                                damageBar.centery - healthText.get_height() // 2))

        text = font.render("Score: " + str(round(self.player.score, 0)), 100, white)
        window.blit(text, (windowWidth - text.get_width() - 50, 20))

    # Prikazuje pygame prozor i objekte u njemu
    def redrawWindow(self):
        window.blit(backgroundImages[int(self.backgroundImageIndex // 1)], (0, 0))  # Postavlja pozadinu prozora
        self.backgroundImageIndex = (self.backgroundImageIndex + 0.5) % 202

        self.player.draw(window)  # Prikazuje igrača u prozoru
        self.enemyCheck()
        self.drawGameStatusInfo()
        pygame.display.update()  # Ažurira prozor kako bi se vidjele napravljene promjene

    # Završava igru i prikazuje završni izbornik
    def gameOver(self):
        pygame.mixer.music.stop()
        gameOverSoundEffect.play(0)
        k = 10
        delay = int(gameOverSoundEffect.get_length() * 1000 // k) - 75
        for i in range(0, k + 1):
            pygame.time.delay(delay)
            rect = pygame.Rect(0, 0, windowWidth, (i + 1) * windowHeight // k)
            pygame.draw.rect(window, black, rect)
            pygame.display.update()

        pygame.quit()
        ender = Ender(Tk(), round(self.player.score, 0))
        ender.mainloop()

    # ------------------------ MAIN PETLJA ------------------------ #
    def main(self):
        pygame.time.delay(200)
        pygame.mixer.music.play(-1)
        while self.run:
            self.clock.tick(framerate)  # Postavlja framerate igre
            self.frameCounter += 1

            # Petlja koja prolazi kroz evente koje generira korisnik
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Provjerava je li korisnik klikuo na X za izlaz iz igre
                    self.run = False

            # Poziva određene funkcije ovisno o pritisnutoj tipki
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.moveLeft()
            if keys[pygame.K_RIGHT]:
                self.player.moveRight()
            if keys[pygame.K_UP]:
                self.player.moveUp()
            if keys[pygame.K_DOWN]:
                self.player.moveDown()
            if keys[pygame.K_ESCAPE]:
                self.run = False

            # Animacija ulaska igrača u prozor - pomiče igrača od dna do sredine prozora
            if self.player.y > windowHeight / 2 and not(self.isPlaying):
                self.player.moveUp()
            else:
                self.isPlaying = True  # Igrač započinje s igranjem

                # Stvara nove neprijatelje kada stari nestanu iz vidljivog područja prozora
                if len(self.enemies) < self.maxEnemyNumber:
                    enemy = Enemy()
                    self.enemies.append(enemy)
                    # Povećava maksimalan broj neprijatelja do 20 svake sekunde (svakih 60 frameova)
                    if self.maxEnemyNumber < 20 and not(self.frameCounter % 60):
                        self.maxEnemyNumber += 0.5

            self.redrawWindow()

            # TODO: napraviti game over izbornik
            if self.isGameOver:
                self.gameOver()
                break