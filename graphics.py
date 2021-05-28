
import sys, pygame
pygame.init()
import time

global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive, var_int

width = 400;
height = 400

white = (225,255,255)
green = (0,255,0)
blue = (0,0,128)

screen = pygame.display.set_mode((width, height))
font = pygame.font.Font('freesansbold.ttf',32)

def intro_screen():
  pygame.display.set_caption('LOADING...')
  image = pygame.image.load("largewagon.jpeg")
  x = 10
  y = 20

  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)

def main_title():
  x = 10
  y = 20
  pygame.display.set_caption('Python Trail')
  image = pygame.image.load("largewagon.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)

def general_store():
  x = 10
  y = 20
  pygame.display.set_caption('Python Trail')
  image = pygame.image.load("Town.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(5)





