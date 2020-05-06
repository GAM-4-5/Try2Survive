from Config import *
def loadData():
    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Definira pygame prozor u fullscreen modeu
    window = pygame.display.set_mode((windowWidth, windowHeight))  # Definira pygame prozor i njegove dimenzije
    pygame.display.set_caption("Try2Survive")  # Postavlja naslov pygame prozora

    backgroundImageNames = ['Assets/background/space' + str(i) + '.png' for i in range(1, 203)]  # Imena pozadinskih slika
    backgroundImages = [pygame.transform.scale(pygame.image.load(image).convert_alpha(),
                                               (windowWidth, windowHeight)) for image in backgroundImageNames]  # Import pozadine

    # Import slika eksplozije
    explosion = [pygame.image.load('Assets/explosion/explosion1.png'), pygame.image.load('Assets/explosion/explosion2.png'),
                 pygame.image.load('Assets/explosion/explosion3.png'), pygame.image.load('Assets/explosion/explosion4.png'),
                 pygame.image.load('Assets/explosion/explosion5.png'), pygame.image.load('Assets/explosion/explosion6.png')]

    backgroundTrack = pygame.mixer.music.load('Assets/audio/backgroundTrack.wav')  # Import pozadinske melodije
    pygame.mixer.music.set_volume(0.3)  # Razina zvuka pozadinske melodije

    playerHitSoundEffect = pygame.mixer.Sound('Assets/audio/explosion.wav')  # Import zvučnog efekta eksplozije
    playerHitSoundEffect.set_volume(0.8)  # Razina zvuka eksplozije

    gameOverSoundEffect = pygame.mixer.Sound('Assets/audio/game_over.wav')  # Import zvučnog efekta za kraj igre
    gameOverSoundEffect.set_volume(0.8)  # Razina zvuka za kraj igre

    font = pygame.font.SysFont("avenirnextttc", 30, True, True)
    fontGameMenu = pygame.font.SysFont("americantypewriterttc", 30)

# window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Definira pygame prozor u fullscreen modeu
window = pygame.display.set_mode((windowWidth, windowHeight))  # Definira pygame prozor i njegove dimenzije
pygame.display.set_caption("Try2Survive")  # Postavlja naslov pygame prozora

backgroundImageNames = ['Assets/background/space' + str(i) + '.png' for i in range(1, 203)]  # Imena pozadinskih slika
backgroundImages = [pygame.transform.scale(pygame.image.load(image).convert_alpha(),
                                           (windowWidth, windowHeight)) for image in
                    backgroundImageNames]  # Import pozadine

# Import slika eksplozije
explosion = [pygame.image.load('Assets/explosion/explosion1.png'), pygame.image.load('Assets/explosion/explosion2.png'),
             pygame.image.load('Assets/explosion/explosion3.png'), pygame.image.load('Assets/explosion/explosion4.png'),
             pygame.image.load('Assets/explosion/explosion5.png'), pygame.image.load('Assets/explosion/explosion6.png')]

backgroundTrack = pygame.mixer.music.load('Assets/audio/backgroundTrack.wav')  # Import pozadinske melodije
pygame.mixer.music.set_volume(0.3)  # Razina zvuka pozadinske melodije

playerHitSoundEffect = pygame.mixer.Sound('Assets/audio/explosion.wav')  # Import zvučnog efekta eksplozije
playerHitSoundEffect.set_volume(0.8)  # Razina zvuka eksplozije

gameOverSoundEffect = pygame.mixer.Sound('Assets/audio/game_over.wav')  # Import zvučnog efekta za kraj igre
gameOverSoundEffect.set_volume(0.8)  # Razina zvuka za kraj igre

font = pygame.font.SysFont("avenirnextttc", 40, True, True)
fontGameStatusBar = pygame.font.SysFont("avenirnextttc", 30, True, True)