
from random import randrange    #Import random
import time 
from graphics import *
from data import *
import sys, pygame
pygame.init()











def get_name():  
  global name      
  name = str(input("What is your name?"))
  print("Your name is,",name)
  
  
  town = pygame.image.load("Town.jpeg")
  

def get_age():
  global age
  age = str(input("Please enter your age:"))
  print("Your age is:",age)
  
def charachter_setup():
  print("===============")
  print("Welcome to Charachter Customization")
  print("===============")
  print('''What would you like to change about your charachter?
  1. Skin Tone
  2. Hair Color
  3. Eye Color
  4. Acessories

  ''')
  usr_select = int(input("Please enter the corresponding number: "))

  if usr_select == 1:
    print("You have selected to change your charachters skin color")
    skin_tone = str(input("What skin tone would you like?:"))
    print("You have chosen:",skin_tone,"Skin Tone")
  elif usr_select == 2:
    print("You have selected to change your charachters hair color")
    hair_color = str(input("What hair color would you like?:"))
    print("You have selected:",hair_color,"Hair")
  elif usr_select == 3:
    print("You have selected to change your charachters eye color")
    eye_color = str(input("What eye color would you like?"))
    print("You have selected:",eye_color,"eye color")
  elif usr_select == 4:
    print("You have selected to change acessories")
    print('''
    You can select the following accessories:
    1.Hat
    2.Glasses
    3.Watch
    4.Mask
    
    ''')
    acessories = str(input("What accessory would you like (Input Number"))
    if acessories == 1:
      print("You have slected a hat")
      hat_type = str(input("What type of hat would you like"))
      print("You have selected",hat_type,"Hat")
      hat_color = str(input("What type of hat color would you like"))
      print("You have selected a",hat_color,"Hat")
    elif acessories == 2:
      print("You have selected Glasses")
      print('''
      What type of glasses would you like?

      1. Wire-Frame Glasses
      2. Monocole
      3. Regular Glasses
      ''')
      glasses_type = str(input("What type of glasses would you like"))
      print("You have selected", glasses_type, "Glasses")
      if glasses_type == 1:
        print("You have selected Wire-Frame Glasses")
      elif glasses_type == 2:
        print("You have selected a monocole")
      elif glasses_type == 3:
        print("You have selected Regular Glasses")
      else:
        print("INVALID INPUT")
    elif acessories == 3:
      print("You ahve selected a Watch")



  

#END

def game_varsetup():     #Buy Supplies
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive,var_int,location_start,location_end,axle_amnt,wheel_amnt,bolt_amnt
  dollars = 700
  general_store()


  print("You have",dollars, "PyCoin to spend")
  amnt_food = int(input("Please enter the amount of food you wish to have(food costs $10 per pound):"))
  print("You have chosen to buy", amnt_food,"Pounds of food")
  dollars = dollars-amnt_food * 10
  print("You have,",dollars,"PyCoin remaining")
  amnt_water = int(input("Please enter the amount of water you wish to carry(Water 1 Dollar per gallon):"))
  print("You purchased:",amnt_water,"Water")
  dollars = dollars-amnt_water * 2
  print("You have,",dollars,"PyCoin remaining")
  animal = str(input("Please enter the animal you would like to pull your wagon-singular:"))
  animal =animal+"s"
  print("You Have Chosen:",animal,"To pull your wagon")
  animal_amnt = int(input("Please enter the number of animals you wish to pull your wagon ($15)"))  
  print("You purchased,",animal_amnt,"Animals")
  dollars = dollars-animal_amnt
  print("You have,",dollars,"PyCoin Remaining")
  axle_amnt = int(input("Please enter the number of axles you would like to purchase:"))
  print("You have bought:",axle_amnt)
  dollars = dollars - axle_amnt *2
  print("You have:",dollars,"Pycoin Remaining")
  wheel_amnt = int(input("Please enter the number of wheels you would like to purchase"))
  print("You have bought:",wheel_amnt,"wheels")
  dollars = dollars - wheel_amnt *3
  print("You have,",dollars,"Pycoin Remaining")
  bolt_amnt = int(input("Please input the number of bolts that you wish to have:"))
  dollars = dollars - bolt_amnt * 2
  print("You have:",dollars,"PyCoin Remaining")
  medicine_amnt = int(input("Please enter the amount of medicine you wish to buy ($10)"))
  print("You have purchased,",medicine_amnt,"Medicine")
  dollars = dollars - medicine_amnt * 10
  print("You have:",dollars,"PyCoin Remaining")
  location_start = str(input("Where would you like to start: "))
  print("You will start in:",location_start)
  location_end = str(input("Where would you like to end:"))
  print("You will start in:",location_end)
  print("\n\n\n")
  var_int = False


#END




def start_game():
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive,var_int,location_end, location_start, axle_amnt, bolt_amnt, wheel_amnt
  print("LOADING...")
  print("===============")
  print("You begin in",location_start,"and Travel to",location_end)
  total_distance = 0        #Distance in total, this willbe length of journey
  total_distance = randrange(500,2001,1)       #500-2000 miles, intervals of 1
  print("You have",total_distance,"Miles to Travel")
  distance_traveled = 0                   #How far you went
  distance_traveled = randrange(1,21,1)   #1-20 miles, intervals of 1
  wagon_dist_traveled = 0                 #Distance traveled by wagon
  alive = True

  
  print("You traveled",distance_traveled," Miles On the first day")
  wagon_dist_traveled =  wagon_dist_traveled + distance_traveled

  while wagon_dist_traveled <= total_distance and alive:
    random_action = 0
    random_action = randrange(1,33,1)
    distance_traveled = 0                   #How far you went
    distance_traveled = randrange(1,21,1)
    wagon_dist_traveled = wagon_dist_traveled + distance_traveled
    print("*****TRAVELING*****")
    random_terr = randrange(1,6,1)

    if random_terr == 1:
      desert()
    elif random_terr == 2:
      jungle()
    elif random_terr == 3:
      mountians()
    elif random_terr == 4:
      forest()
    elif random_terr == 5:
      grassland()
    time.sleep(1.25)
    print("You have Traveled:",wagon_dist_traveled,"Miles In Total")
    print("You traveled,", distance_traveled,"Miles Today")
    miles_left = total_distance - wagon_dist_traveled
    print("You have",miles_left,"Miles left to travel")
    if amnt_food >= 1:
      random_food_subtract = randrange(0,4,1)
      amnt_food = amnt_food - random_food_subtract
      print("You eat,",random_food_subtract,"Today")
      print("You have:",amnt_food)
    else:
      print("You are out of food")
  
    if random_action ==1:
      cholera = True
      cholera_graphics()
      print("===============")
      print( name,"has contracted Cholera")
      user_choice = ""
      user_choice = str(input("Would you like to use medicine or continue(Type medicine or Continue)"))
      if (user_choice == "medicine" or user_choice == "med" or user_choice == "Medicine") :
        print("You are Cured!")
        cholera = False
        print("===============")
      else:
        print( name,"has died!")
        print("Game Over!")
        print("===============")
        alive_false()
        alive = False

    if random_action == 2:
      wagon_broken = True
      print("===============")
      print("Your Wagon has broken down")
      wagon_broken_graphics()
      user_choice = str(input("Would you like to use spare parts or continue?(Spare or Continue"))
      random_parts = randrange(0,4,1)
      if random_parts == 0 and axle_amnt >= 1:
        print("The axle on your wagon breaks")
        axle_amnt = axle_amnt - 1
        print("You have:",axle_amnt,"Axles remaining")
      elif random_parts == 1 and wheel_amnt >= 1:
        print("The Wheel on your wagon breaks")
        wheel_amnt = wheel_amnt - 1
        print("You have",wheel_amnt,"Wheels remaining")
      elif random_parts == 2 and wheel_amnt >= 2:
        print("The bolt on your wagon breaks")
        bolt_amnt = bolt_amnt - 1
        print("You have:",bolt_amnt)
      else: 
        amnt_food = amnt_food - 2
        print("You lose 2 food from wild animals")
        print("You have:",amnt_food,"food left")
        wild_animals()
        print("===============")

    
        
    if random_action == 4:
      python_encountered = True
      print("===============")
      print("You have encountered a python")
      user_choice = str(input("Would you like to continue or try to hunt the python(hunt or continue)"))
      hunt_random = randrange(0,8,1)
      if (user_choice == "hunt" or user_choice == "Hunt" or user_choice == "hnt"):
        print("You attempt to hunt the python")
          
      
      word_len = int(input("How long of a word would you like to type: "))
      if word_len <= 3:
        print("Invalid")
      elif word_len == 4:

        print("Length of 4 Selected")
        four_letter = "Cool", "Nice", "Jazz", "Able", "Baby", "Band", "Have"
        random_word = four_letter[hunt_random]
        print("Please Type:", random_word)
        print("Ready")
        time.sleep(1)
        print("Set")
        time.sleep(1)
        print("Go")
        current_time = time.time()
        future = current_time + 2
        word = str(input("Please enter the word:"))
        current_time = time.time()
        if word == random_word and current_time < future:
          print("You have Captured the Python")
          print("You add two food")
          amnt_food = amnt_food + 2
          print("You have:",amnt_food,"Food in total")
        else:
          print("You have not captured the Python")
      elif word_len == 5:
        print("Length of 5 Selected")
        five_letter = "Water","Horse","Python", "Beast","Cards", "Blues","Travel"
        random_word = five_letter[hunt_random]
        print("Please Type:", random_word)
        print("Ready")
        time.sleep(1)
        print("Set")
        time.sleep(1)
        print("Go")
        current_time = time.time()
        future = current_time + 2
        word = str(input("Please enter the word:"))
        current_time = time.time()
        if word == random_word and current_time > future:
          print("You have Captured the Python")
          print("You add two food")
          amnt_food = amnt_food + 2
          print("You have:",amnt_food,"Food in total")
        else:
          print("You have not captured the Python")
        

      elif word_len == 6:
        print("Length of six Selected")
        print("Length of 5 Selected")
        six_letter = "Settler","Abroad","Afraid","Appear","Camera","Castle","Garden"
        random_word = six_letter[hunt_random]
        print("Please Type:", random_word)
        print("Ready")
        time.sleep(1)
        print("Set")
        time.sleep(1)
        print("Go")
        current_time = time.time()
        future = current_time + 2
        word = str(input("Please enter the word:"))
        current_time = time.time()
        if word == random_word and current_time > future:
          print("You have Captured the Python")
          print("You add two food")
          amnt_food = amnt_food + 2
          print("You have:",amnt_food,"Food in total")
        else:
          print("You have not captured the Python")
      else:
        print("Invalid")
      

  
    
    if random_action ==5:
      print("===============")
      town_encountered_graphics()
      end_visit = False
      print("You have encountered a town!")
      user_choice = str(input("Would you like to continue or stop and buy Supplies (Continue or Stop)"))
      if user_choice == "stop" or user_choice == "Stop" or user_choice =="stp":
        what_buy = str(input("What Item would you like to buy? (Medicine, Food, Water, Animals)"))
        if (what_buy == "Med" or what_buy == "Medicine" or what_buy == "medicine" or what_buy == "med") and dollars > 15:
          print("You have chosen to buy medicine")
          print("You have:",dollars,"PyCoin Left")
          medicine_add = int(input("How much Medicine do you wish to buy?"))
          if medicine_add == "Quit" or medicine_add == "Qut" or medicine_add == "quit":
            print("You have chosen to Quit")
          medicine_amnt = medicine_amnt + medicine_add
          dollars = dollars - medicine_add * 10
          print("You have:",dollars, "PyCoin Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "Food" or what_buy == "fd" or what_buy == "food") and dollars > 15:
          print("You Have Chosen to buy food")
          print("You have:",dollars,"Dollars Left")
          food_add = str(input("How much food do you wish to buy?"))
          if food_add == "Quit" or food_add == "Qut" or food_add == "quit":
            print("You have chosen to Quit")
          amnt_food  = amnt_food - food_add
          dollars = dollars - food_add * 10
          print("You have:",dollars, "PyCoin Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "wtr" or what_buy == "Water" or what_buy == "water") and dollars > 15:
          print("You have chosen to buy water")
          print("You have:",dollars,"PyCoin Left") 
          water_add = int(input("How much water do you want to buy?:"))
          if water_add == "Quit" or water_add == "Qut" or water_add == "quit":
            print("You have chosen to Quit")
          water_amnt = water_amnt + water_add
          dollars = dollars - water_add * 1
          print("You have:",dollars, "PyCoin Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "Animal" or what_buy == "animal" or what_buy == "anm") and dolars > 15:
          print("You have chosen to buy Animals")
          print("You have:",dollars,"PyCoin Left") 
          animal_add = int(input("How many animals do you want to buy?:"))
          if animal_add == "Quit" or animal_add == "Qut" or animal_add == "quit":
            print("You have chosen to Quit")
          dollars = dollars - animal_add * 15
          print("You have:",dollars, "PyCoin Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")

          
        

    if random_action ==7:
      print("===============")
      print("You have encountered a river")
      river_encountered_graphics()
      river_encountered = True
      user_choice = str(input("Would you like to swim or ford the river, or wait(cross,swim,wait)"))

      if (user_choice == "ford" or user_choice =="Ford" or user_choice =="frd"):
        frd_random = randrange(0,6,1)
        ford_graphics()
        if frd_random ==0:
          print("You cross the river and lose no supplies")
        elif frd_random ==1:
          print("You ford the river but lose 1 Water")
          water_amnt = water_amnt-1
          print("You have",water_amnt,"Water Left")
        elif frd_random ==2:
          print("You ford the river")
        elif frd_random ==3:
          print("You ford the river but lose 1 spare parts")
          spareprts_amnt = spareprts_amnt - 1
          print("You have",spareprts_amnt,"Spare Parts")
        elif frd_random ==4:
          print("You ford the river")
        else:
          print("You ford the river, but lose 2 animals")
          animal_amnt = animal_amnt - 2
          print("You have",animal_amnt,"Animals left")
      elif (user_choice == "swim" or user_choice == "Swim" or user_choice == "swm"):
        swm_random = randrange(0,2,1)
        river_encountered_graphics()
        if swm_random == 0:
          print("You cross the river")
        else:
          print(name,"Drowned")
          print( name,"has died!")
          print("Game Over!")
          print("===============")
          alive = False
          alive_false()
      elif (user_choice == "wait" or user_choice =="Wait" or user_choice == "wt"):
        print("*****WAITING*****")
        time.sleep(5)
        animal_amnt = animal_amnt - 2
        river_encountered_graphics()

        print("While you waited, 2 animals died")
        print("You have",animal_amnt,animal,"Animals Left")

    if random_action == 9:
      print("===============")
      print("You encounter Bandits on your journey")
      bandit_random = randrange(1,5,1)
      type_of_item = randrange(1,5,1)
      if type_of_item == 1 and amnt_food > 4:
        food_stolen = bandit_random
        amnt_food = amnt_food - food_stolen
        print("The bandits steal", food_stolen,"Food")
        print("You have:",amnt_food,"Food Left")
      elif type_of_item == 2 and amnt_water > 4:
        water_stolen = bandit_random
        amnt_water = amnt_water - water_stolen
        print("The bandits steal", water_stolen, "Water")
        print("You have:",amnt_water,"Water Left")
      elif type_of_item == 3 and medicine_amnt > 4:
        medicine_stolen = bandit_random
        medicine_amnt = medicine_amnt - medicine_stolen
        print("The bandits steal:",medicine_stolen,"Medicine")
        print("You have:",medicine_amnt,"Medicine Left")
      elif type_of_item == 4 and animal_amnt > 4:
        animals_stolen = bandit_random
        animal_amnt = animal_amnt - bandit_random
        print("The bandits Steal:",animals_stolen,"Animals")
        print("You have:",medicine_amnt,"Medicine")
    
    if random_action == 11:
      storm_graphics()
      print("===============")
      print("You have encountered a severe storm. You must wait one day.")
      print("*****WAITING*****")
      time.sleep(5)

    if random_action == 13:
      print("===============")
      random_injury = randrange(1,4,1)
      random_injury_graphics()
      if random_injury == 1:
        survive = randrange (1,3,1)
        print("You have contracted Dysentary")
        print("There is no medicine")
        if survive == 1:
          print(name,"Has died of dysentary")
        if survive == 2:
          print(name,"Has Survived")
      if random_injury == 2:
        wait_amnt = randrange (1,6,1)
        print(name,"Has a broken arm")
        print("You need to wait",wait_amnt,"Days before you continue")
        if wait_amnt == 1:
          print("*****WAITING*****")
          time.sleep(1)
        elif wait_amnt == 2 and amnt_food > 4:
          print("*****WAITING*****")
          time.sleep(1)
          stole_amnt = randrange(1,4,1)
          print("While you were sleeping, animals stole",stole_amnt, "Food")
          amnt_food = amnt_food - stole_amnt
          print("You have:",amnt_food,"Food Left")
        elif wait_amnt == 3:
          print("You encounter inclement weather and you must wait")
          print("*****WAITING*****")
          time.sleep(3)
        elif wait_amnt == 4 and amnt_water > 4:
          print("You encounter inclement weather and must wait")
          print("*****WAITING*****")
          time.sleep(4)
          stole_amnt = randrange(1,4,1)
          print("While you were sleeping, animals stole:",stole_amnt, "Water")
          amnt_water = amnt_water - stole_amnt
          print("You have",amnt_water,"Water Left")
        elif wait_amnt ==5:
          print("You encounter inclement weather and must wait")
          print("*****WAITING*****")
          time.sleep(5)
        elif wait_amnt == 6 and animal_amnt > 4:
          print("*****WAITING*****")
          time.sleep(6)
          stole_amnt = randrange(1,4,1)
          print("While you were waiting animals came and ate:",stole_amnt,"Animals")
          animal_amnt = animal_amnt - stole_amnt
          print("You have:", animal_amnt, "Animals Left")
      if random_injury == 3:
        typhoid = True
        print("===============")
        print( name,"has contracted Typhoid ")
        user_choice = ""
        user_choice = str(input("Would you like to use medicine or continue(Type medicine or Continue)"))
        if (user_choice == "medicine" or user_choice == "med" or user_choice == "Medicine") :
          print("You are Cured!")
          typhoid = False
          print("===============")
        else:
          print( name,"has died!")
          print("Game Over!")
          print("===============")
          alive = False

    if random_action == 15:
      print("===============")
      flood_graphics()
      print("There is a flood on the trail, and you must go around.")
      add_dist = randrange(1,51,1)
      total_distance = total_distance + add_dist
      print("You add",add_dist,"To your journey")
      print("You have",total_distance,"Miles Left to travel")
      

    if random_action == 17:
      print("===============")
      wagon_abandoned_graphics()
      print("You find an abandoned wagon on the trail")
      abandoned_wagon = randrange(1,4,1)
      abandoned_wagon_supplies = randrange(1,16,1)

      if abandoned_wagon == 1:
        print("You find:",abandoned_wagon_supplies,"Food")
        amnt_food = amnt_food + abandoned_wagon_supplies
        print("You have",amnt_food,"Total Food")
      elif abandoned_wagon == 2:
        print("You find:",abandoned_wagon,"Water")
        amnt_water = amnt_water + abandoned_wagon_supplies
        print("You have:",amnt_water,"Total")
      else:
        print("You find:",abandoned_wagon,"Medicine")
        medicine_amnt = medicine_amnt + abandoned_wagon
        print("You have", medicine_amnt, "Total")

    if random_action == 19:
      setller_encounter = True
      end_visit = False
      settler_camp_graphics()
      print("===============")
      print("You have encountered a Settler Camp!")
      user_choice = str(input("Would you like to continue or stop and buy Supplies (Continue or Stop)"))
      if user_choice == "stop" or user_choice == "Stop" or user_choice =="stp":
        what_buy = str(input("What Item would you like to buy? (Medicine, Food, Water, Animals)"))
        if (what_buy == "Med" or what_buy == "Medicine" or what_buy == "medicine" or what_buy == "med") and dollars > 15:
          print("You have chosen to buy medicine")
          print("You have:",dollars,"PyCoin Left")
          medicine_add = int(input("How much Medicine do you wish to buy?"))
          if medicine_add == "Quit" or medicine_add == "Qut" or medicine_add == "quit":
            print("You have chosen to Quit")
          medicine_amnt = medicine_amnt + medicine_add
          dollars = dollars - medicine_add * 10
          print("You have:",dollars, "Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "Food" or what_buy == "fd" or what_buy == "food") and dollars > 15:
          print("You Have Chosen to buy food")
          print("You have:",dollars,"PyCoin Left")
          food_add = str(input("How much food do you wish to buy?"))
          if food_add == "Quit" or food_add == "Qut" or food_add == "quit":
            print("You have chosen to Quit")
          amnt_food  = amnt_food - food_add
          dollars = dollars - food_add * 10
          print("You have:",dollars, "PyCoin Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "wtr" or what_buy == "Water" or what_buy == "water") and dollars > 15:
          print("You have chosen to buy water")
          print("You have:",dollars,"PyCoin Left") 
          water_add = int(input("How much water do you want to buy?:"))
          if water_add == "Quit" or water_add == "Qut" or water_add == "quit":
            print("You have chosen to Quit")
          water_amnt = water_amnt + water_add
          dollars = dollars - water_add * 1
          print("You have:",dollars, "Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "Animal" or what_buy == "animal" or what_buy == "anm") and dolars > 15:
          print("You have chosen to buy Animals")
          print("You have:",dollars,"PyCoin Left") 
          animal_add = int(input("How many animals do you want to buy?:"))
          if animal_add == "Quit" or animal_add == "Qut" or animal_add == "quit":
            print("You have chosen to Quit")
          dollars = dollars - animal_add * 15
          print("You have:",dollars, "Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
      
      if random_action == 21:
        print("===============")
        bufallo_graphics()
        print("You encounter a herd of bufallo")
        if (user_choice == "hunt" or user_choice == "Hunt" or user_choice == "hnt"):
          word_len = int(input("How long of a word would you like to type: "))
      if word_len <= 3:
        print("Invalid")
      elif word_len == 4:

        print("Length of 4 Selected")
        four_letter = "Cool", "Nice", "Jazz", "Able", "Baby", "Band", "Have"
        random_word = four_letter[hunt_random]
        print("Please Type:", random_word)
        print("Ready")
        time.sleep(1)
        print("Set")
        time.sleep(1)
        print("Go")

        word = str(input("Please enter the word:"))
        current_time = time.time()
        future = current_time + 2
        if word == random_word and current_time < future:
          print("You have Captured the Buffallo")
          print("You add two food")
          amnt_food = amnt_food + 2
          print("You have:",amnt_food,"Food in total")
        else:
          print("You have not captured the Buffallo")
      elif word_len == 5:
        print("Length of 5 Selected")
        five_letter = "Water","Horse","Python", "Beast","Cards", "Blues","Travel"
        random_word = five_letter[hunt_random]
        print("Please Type:", random_word)
        print("Ready")
        time.sleep(1)
        print("Set")
        time.sleep(1)
        print("Go")
        word = str(input("Please enter the word:"))
        current_time = time.time()
        future = current_time + 2
        if word == random_word and current_time > future:
          print("You have Captured the Bufallo")
          print("You add two food")
          amnt_food = amnt_food + 2
          print("You have:",amnt_food,"Food in total")
          print("===============")
        else:
          print("You have not captured the Buffallo")
          print("===============")
        

      elif word_len == 6:
        print("Length of six Selected")
        print("Length of 5 Selected")
        six_letter = "Settler","Abroad","Afraid","Appear","Camera","Castle","Garden"
        random_word = six_letter[hunt_random]
        print("Please Type:", random_word)
        print("Ready")
        time.sleep(1)
        print("Set")
        time.sleep(1)
        print("Go")
        word = str(input("Please enter the word:"))
        current_time = time.time()
        future = current_time + 2
        if word == random_word and current_time > future:
          print("You have Captured the Python")
          print("You add two food")
          amnt_food = amnt_food + 2
          print("You have:",amnt_food,"Food in total")
        else:
          print("You have not captured the Python")
      else:
        print("Invalid")

      if random_action == 23:
        print("===============")
        money_graphics()
        print("You find some settlers who offer to give you money if you help them")
        money_amnt_wanted = int(input("How much money would you like to earn?:"))
        if money_amnt_wanted >=20:
          print("Too much money entered! Please Try Again")
          money_amnt_wanted = int(input("How much money would you like to earn?:"))
        elif money_amnt_wanted <20:
          print("You wish to earn:", money_amnt_wanted,"dollars")
          random_word = randrange(0,18,1)
          farm_words = "Sow" , "Food", "Horse", "Cow", "Plant", "Bee", "Boar","Buffallo","Calf","Chick","Coop","Egg","Ewe","Sheep","Chicken","Goat","Gander"
          word = str(input("Please type the word",farm_words[random_word],": "))
          if word == farm_words[random_word]:
            print("You have earned 1 Dollar")
            dollars = dollars + 1
            print("You have:",dollars,"In total")
            money_amnt_wanted = money_amnt_wanted - 1
            while money_amnt_wanted != 0:
              random_word = randrange(0,18,1)
              farm_words = "Sow" , "Food", "Horse", "Cow", "Plant", "Bee", "Boar","Buffallo","Calf","Chick","Coop","Egg","Ewe","Sheep","Chicken","Goat","Gander"
              word = str(input("Please type the word",farm_words[random_word],": "))
              if word == farm_words[random_word]:
                print("You have earned 1 Dollar")
                dollars = dollars + 1
                print("You have:",dollars,"In total")
                money_amnt_wanted = money_amnt_wanted - 1
          else:
            print("You did not enter the word correctly")
            user_choice = str(input("Would you like to try again?(y or n)"))

            if user_choice == "Y" or user_choice == "y":
              random_word = randrange(0,18,1)
              farm_words = "Sow" , "Food", "Horse", "Cow", "Plant", "Bee", "Boar","Buffallo","Calf","Chick","Coop","Egg","Ewe","Sheep","Chicken","Goat","Gander"
              word = str(input("Please type the word",farm_words[random_word],": "))
              if word == farm_words[random_word]:
                print("You have earned 1 Dollar")
                dollars = dollars + 1
                print("You have:",dollars,"In total")
                money_amnt_wanted = money_amnt_wanted - 1
                while money_amnt_wanted != 0:
                  random_word = randrange(0,18,1)
                  farm_words = "Sow" , "Food", "Horse", "Cow", "Plant", "Bee", "Boar","Buffallo","Calf","Chick","Coop","Egg","Ewe","Sheep","Chicken","Goat","Gander"
                  word = str(input("Please type the word",farm_words[random_word],": "))
                if word == farm_words[random_word]:
                  print("You have earned 1 Dollar")
                  dollars = dollars + 1
                  print("You have:",dollars,"In total")
                  money_amnt_wanted = money_amnt_wanted - 1
              if user_choice == "N" or user_choice == "n":
                print("You continue on")



        else:
          print("Invalid Amount Entered.Please Try Again")   
          money_amnt_wanted = int(input("How much money would you like to earn?:"))   


      if random_action == 26 and amnt_food > 4:
        print("===============")
        print("Some of your food gets moldy")
        food_lost = randrange(1,5,1)
        print("You lose:",food_lost,"Food")
        amnt_food = amnt_food - food_lost
        print("You have",amnt_food,"Food remaining")

      if random_action == 29 and amnt_water > 4:
        print("===============")
        print("Some of your water gets stagnant")
        water_lost = randrange(1,5,1)
        print("You lose:",food_lost,"water")
        amnt_water = amnt_water - water_lost
        print("You have",amnt_water,"Water remaining")

      if random_action == 32:
        print("===============")
        print("You lose the trail and are uncertain which way to go")
        print('''
        You have 4 options
        1.Go North
        2.Go South
        3.Go East
        4.Go west 
        
        ''')

        random_direction = randrange(0,4,1)
        correct_choice = randrange(0,2,1)
        distance_add = randrange(0,26,1)
        usr_dir_choice = str(input("Please enter which way you wish to go: "))
        if usr_dir_choice == "North" and random_direction == 0:
          if correct_choice == 0:
            print("You have chosen the wrong way")
            print("You go back")
            
            distance_traveled = distance_traveled + distance_add
            print("You have traveled:",distance_traveled)
          else:
            print("You have chosen the correct way")
            print("You continue on")
        if usr_dir_choice == "South" and random_direction == 1:
          if correct_choice == 0:
            print("You have chosen the correct way")
            print("You go back")
            
            distance_traveled = distance_traveled + distance_add
            print("You have traveled:",distance_traveled)
          else:
            print("This is the correct way")
            print("You continue on")
        if usr_dir_choice == "East" and random_direction == 2:
          if correct_choice == 0:
            print("You have chosen the wrong way")
            print("You go back")
            
            distance_traveled = distance_traveled + distance_add
            print("You have traveled:",distance_traveled)
          else:
            print("This is the correct way")
            print("You continue on")
        if usr_dir_choice == "West" and random_direction == 3:
          if correct_choice == 0:
            print("You have chosen the wrong way")
            print("You go back")
            
            distance_traveled = distance_traveled + distance_add
            print("You have traveled:",distance_traveled)
          else:
            print("This is the correct way")
            print("You continue on")



          

        


        



      

        




        
      


    
        





         


def end_game():
  print("===============")
  print("You have completed your journey")

def end_game_fail():
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive, var_int, location_start, location_end
  print("===============")
  print("You have not successfuly completed your journey")
  user_choice = str(input("Would you like to play again? (y or n):"))
  if user_choice == "Yes" or user_choice == "y" or user_choice == "Y":
    print("You have chosen to play again")
    intro_screen()
    main_title()
    get_name()
    get_age()
    charachter_setup()
    game_varsetup()
    start_game()
  else:
    print("Thank you for playing Python Trail")

  
def main():
  #END
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive,var_int,location_start,location_end, wheel_amnt, axle_amnt, bolt_amnt
  
  print("Welcome to Python Trail")         #Running different functions, Main body
  print("===============")
  intro_screen()
  main_title()
  get_name()
  get_age()
  charachter_setup()
  game_varsetup()
  start_game()
  if alive == True:
    end_game()
  else:
    end_game_fail()


global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive, var_int, location_start, location_end
main()







