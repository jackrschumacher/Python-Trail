from replit import db
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

def desert():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("desert.jpg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  

def forest():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("forest.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def jungle():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("jungle.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()


def mountians():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("mountain.jpg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def grassland():
  x = 10
  y = 20
  pygame.display.set_caption('Traveling')
  screen.fill((0,0,0))
  image = pygame.image.load("grassland.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def town_encountered_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('You have encountered a Town!')
  screen.fill((0,0,0))
  image = pygame.image.load("Town.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def hunt():
  
  db["Four_Letter"] = "Test","Able","Band","Care","Cast","Cool","Nice","Know","Hunt","Zone"
  x = 10
  y = 20
  pygame.display.set_caption('Python')
  screen.fill((0,0,0))
  image = pygame.image.load("python.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()




  '''
  dis = pygame.display.set_mode((400,300))
  pygame.display.update()
  pygame.display.set_caption('Hunting')

  
  game_over = False

  def message(msg,color):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

  while game_over == False:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x1_change = -10
          y1_change = 0
        elif event.key == pygame.K_RIGHT:
          x1_change = 10
          y1_change = 0
        elif event.key == pygame.K_UP:
          y1_change = -10
          x1_change = 0
        elif event.key == pygame.K_DOWN:
          y1_change = 10
          x1_change = 0
  #https://www.edureka.co/blog/snake-game-with-pygame/
  x1 += x1_change
  y1 += y1_change
  dis.fill(white)

  pygame.draw.rect(dis,blue,[200,150,10,10])
  pygame.display.update()
  quit()
'''

def cholera_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Cholera')
  screen.fill((0,0,0))
  image = pygame.image.load("cholera.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def alive_false():
  x = 10
  y = 20
  pygame.display.set_caption('Game Over')
  screen.fill((0,0,0))
  image = pygame.image.load("skull.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  time.sleep(3)
  x = 10
  y = 20
  pygame.display.set_caption('Game Over')
  screen.fill((0,0,0))
  image = pygame.image.load("gameover.png")
  screen.blit(image,(x,y))
  pygame.display.flip()

def wagon_broken_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Wagon Broken')
  screen.fill((0,0,0))
  image = pygame.image.load("wagonbroken.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def wild_animals():
  x = 10
  y = 20
  pygame.display.set_caption('Wild Animals')
  screen.fill((0,0,0))
  image = pygame.image.load("wild_animals")
  screen.blit(image,(x,y))
  pygame.display.flip()

def river_encountered_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('River')
  screen.fill((0,0,0))
  image = pygame.image.load("river.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def ford_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Ford')
  screen.fill((0,0,0))
  image = pygame.image.load("barge.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def bandits_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Bandits')
  screen.fill((0,0,0))
  image = pygame.image.load("bandits.png")
  screen.blit(image,(x,y))
  pygame.display.flip()

def storm_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Storm')
  screen.fill((0,0,0))
  image = pygame.image.load("stormgraphics.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()
  
def random_injury_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Injury')
  screen.fill((0,0,0))
  image = pygame.image.load("injury.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def flood_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Flood')
  screen.fill((0,0,0))
  image = pygame.image.load("flood.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()


  
def wagon_abandoned_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Abandoned Wagon')
  screen.fill((0,0,0))
  image = pygame.image.load("wagonbroken.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def settler_camp_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Settler Camp')
  screen.fill((0,0,0))
  image = pygame.image.load("tent.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def buffallo_graphics():
  x = 10
  y = 20
  pygame.display.set_caption('Abandoned Wagon')
  screen.fill((0,0,0))
  image = pygame.image.load("wagonbroken.jpeg")
  screen.blit(image,(x,y))
  pygame.display.flip()

def money_graphics():#Add
  x = 10
  y = 20
  pygame.display.set_caption('Money')
  screen.fill((0,0,0))
  image = pygame.image.load("money.png")
  screen.blit(image,(x,y))
  pygame.display.flip()















