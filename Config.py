import pygame
pygame.init()

infoObject = pygame.display.Info()
windowWidth, windowHeight = infoObject.current_w, infoObject.current_h

framerate = 60

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)