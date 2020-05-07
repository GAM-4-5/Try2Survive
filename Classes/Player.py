from Config import *

playerImage = pygame.image.load('Assets/player.png') # Import slike igrača
class Player:
    def __init__(self):
        self.width = 100
        self.height = 100
        self.x = windowWidth / 2
        self.y = windowHeight + self.height
        self.speed = 10
        self.image = pygame.transform.scale(playerImage, (self.width, self.height))
        self.imageAngle = 0
        self.hitbox = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        self.hitCount = 0
        self.health = 500
        self.maxHealth = 500
        self.score = 0

    # Vraća koordinate igrača
    def getCoordinates(self):
        return self.x, self.y

    # Vraća centralne koordinate igrača
    def getCenterCoordinates(self):
        return self.x + self.width / 2, self.y + self.height / 2

    # Crta igrača u prozoru
    def draw(self, window):
        image = pygame.transform.rotate(self.image, self.imageAngle) # Rotira sliku igrača
        window.blit(image, (self.x - int(image.get_width() / 2), self.y - int(image.get_height() / 2))) # Centrira rotiranu sliku
        self.imageAngle = (self.imageAngle + 10) % 360
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        self.hitbox = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

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

    # Vraća osnovne vrijednosti instance klase Player
    def values(self):
        return self.x, self.y, self.width, self.height

    # Vraća bool je li igrač pogođen
    def isHit(self, enemy):
        if self.hitbox.colliderect(enemy.hitbox):
            self.score -= enemy.damage if self.score > enemy.damage else self.score
            self.hitCount += 1
            self.health -= enemy.damage if self.health > enemy.damage else self.health
            return True
        return False
