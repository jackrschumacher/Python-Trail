import sys, pygame
pygame.init()
import time

global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive

width = 300;
height = 300

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
  x = 0
  y = 0
  display_surface = pygame.display.set_mode((x, y))
  pygame.display.set_caption('Python Trail')
  text = font.render('Python Trail',True, green, blue)
  text_rectangle = text.get_rect()
  text_rectangle.center = (x // 2, y // 2)
  display_surface.fill(white)
  display_surface.blit(text,text_rectangle)

