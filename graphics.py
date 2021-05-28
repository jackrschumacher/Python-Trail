
import sys, pygame
pygame.init()
import time
pygame.event.get()
global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive, var_int

width = 400;
height = 400

white = (225,255,255)
green = (0,255,0)
blue = (0,0,128)




screen = pygame.display.set_mode((width, height))


def intro_screen():
  pygame.display.set_caption('LOADING...')
  image = pygame.image.load("loading.jpg")
  x = 10
  y = 20

  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)

mouse_pressed = pygame.mouse.get_pressed()

def main_title():

  x = 10
  y = 20
  pygame.display.set_caption('Python Trail')
  screen.fill((225,255,255))
  image = pygame.image.load("logo.png")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)
  x = 10
  y = 20


def general_store():
  x = 10
  y = 20
  pygame.display.set_caption('General Store')
  screen.fill((0,0,0))
  image = pygame.image.load("Town.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)

def desert():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("desert.jpg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)

def forest():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("forest.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)

def jungle():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("jungle.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)

def mountians():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("mountain.jpg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)





