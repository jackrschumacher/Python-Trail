import sys, pygame
pygame.init()

width = 300;
height = 300

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('LOADING...')
image = pygame.image.load("wagon.png")
x = 10
y = 20

screen.blit(image,(x,y))
pygame.display.flip()
