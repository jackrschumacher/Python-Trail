from random import randrange    #Import random
import time     

def get_name():  
  global name      
  name = str(input("What is your name?"))
  print("Your name is,",name)
  

def get_age():
  global age
  age = str(input("Please enter your age:"))
  print("Your age is:",age)
  
  

#END

def game_varsetup():     #Buy Supplies
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive
  dollars = 400


  print("You have",dollars, "dollars to spend")
  amnt_food = int(input("Please enter the amount of food you wish to have(food costs $10 per pound):"))
  print("You have chosen to buy", amnt_food,"Pounds of food")
  dollars = dollars-amnt_food * 10
  print("You have,",dollars,"dollars remaining")
  amnt_water = int(input("Please enter the amount of water you wish to carry(Water 1 Dollar per gallon):"))
  print("You purchased:",amnt_water,"Water")
  dollars = dollars-amnt_water * 2
  print("You have,",dollars,"dollars remaining")
  animal = str(input("Please enter the animal you would like to pull your wagon-singular:"))
  animal =animal+"s"
  print("You Have Chosen:",animal,"To pull your wagon")
  animal_amnt = int(input("Please enter the number of animals you wish to pull your wagon ($15)"))  
  print("You purchased,",animal_amnt,"Animals")
  dollars = dollars-animal_amnt
  print("You have,",dollars,"Dollars Remaining")
  spareprts_amnt = int(input("Please enter the number of spare parts you wish to have(10)"))
  print("You have,",spareprts_amnt,"Spare Parts")
  dollars = dollars - spareprts_amnt * 10
  print("You purchased:",dollars,"Spare Parts")
  medicine_amnt = int(input("Please enter the amount of medicine you wish to buy ($10)"))
  print("You have purchased,",medicine_amnt,"Medicine")
  dollars = dollars - medicine_amnt * 10
  print("You have:",dollars,"Dollars Remaining")
  print("\n\n\n")


#END




def start_game():
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive
  print("LOADING...")
  print("===============")
  print("You begin in Wisconsin and Travel to Flordia")
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
    random_action = randrange(1,31,1)
    distance_traveled = 0                   #How far you went
    distance_traveled = randrange(1,21,1)
    wagon_dist_traveled = wagon_dist_traveled + distance_traveled
    print("*****TRAVELING*****")
    time.sleep(1.25)
    print("You have Traveled:",wagon_dist_traveled,"Miles In Total")
    print("You traveled,", distance_traveled,"Miles Today")
    miles_left = total_distance - wagon_dist_traveled
    print("You have",miles_left,"Miles left to travel")
    
    if random_action ==1:
      cholera = True
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
        alive = False

    if random_action == 2:
      wagon_broken = True
      print("===============")
      print("Your Wagon has broken down")
      user_choice = str(input("Would you like to use spare parts or continue?(Spare or Continue"))
      if (user_choice == "Spare" or user_choice == "spare" or user_choice == "spr"):
        wagon_broken = False
        print("Your Wagon is Repaired")
        print("===============")
      elif amnt_food ==0:
        print(name,"Starved")
        print( name,"has died!")
        print("Game Over!")
        print("===============")
        alive = False
      elif amnt_food > 0: 
        amnt_food = amnt_food - 2
        print("You lose 2 food from wild animals")
        print("You have:",amnt_food,"food left")
        print("===============")
    
        
    if random_action == 4:
      python_encountered = True
      print("===============")
      print("You have encountered a python")
      user_choice = str(input("Would you like to continue or try to hunt the python(hunt or continue)"))
      hunt_random = randrange(0,3,1)
      if (user_choice == "hunt" or user_choice == "Hunt" or user_choice == "hnt"):
        print("You attempt to hunt the python")
        if hunt_random == 0:
          print("You do not capture the python")
          print("===============")
        elif hunt_random ==1:
          print("You capture the python and eat it")
          print("===============")
          amnt_food = amnt_food+2
        elif hunt_random == 2:
          print("You capture the python, but it escapes")
          print("===============")
      else:
        print("The python comes back when you are sleeping and Kills one of your",animal)
        animal_amnt = animal_amnt-1
        print("You have:",animal_amnt,"left")
        print("===============")
    
    if random_action ==5:
      print("===============")
      town_encountered = True
      end_visit = False
      print("You have encountered a town!")
      user_choice = str(input("Would you like to continue or stop and buy Supplies (Continue or Stop)"))
      if user_choice == "stop" or user_choice == "Stop" or user_choice =="stp":
        what_buy = str(input("What Item would you like to buy? (Medicine, Food, Water, Animals)"))
        if (what_buy == "Med" or what_buy == "Medicine" or what_buy == "medicine" or what_buy == "med") and dollars > 15:
          print("You have chosen to buy medicine")
          print("You have:",dollars,"Dollars Left")
          medicine_add = int(input("How much Medicine do you wish to buy?"))
          medicine_amnt = medicine_amnt + medicine_add
          dollars = dollars - medicine_add * 10
          print("You have:",dollars, "Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "Food" or what_buy == "fd" or what_buy == "food") and dollars > 15:
          print("You Have Chosen to buy food")
          print("You have:",dollars,"Dollars Left")
          food_add = str(input("How much food do you wish to buy?"))
          amnt_food  = amnt_food - food_add
          dollars = dollars - food_add * 10
          print("You have:",dollars, "Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "wtr" or what_buy == "Water" or what_buy == "water") and dollars > 15:
          print("You have chosen to buy water")
          print("You have:",dollars,"Dollars Left") 
          water_add = int(input("How much water do you want to buy?:"))
          water_add = water_amnt + water_add
          dollars = dollars - water_add * 1
          print("You have:",dollars, "Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")
        elif (what_buy == "Animal" or what_buy == "animal" or what_buy == "anm") and dolars > 15:
          print("You have chosen to buy Animals")
          print("You have:",dollars,"Dollars Left") 
          animal_add = int(input("How many animals do you want to buy?:"))
          dollars = dollars - animal_add * 15
          print("You have:",dollars, "Remaining")
          if dollars <=0:
            print("You can not buy anything else, as you are out of money")

          
        

    if random_action ==7:
      print("===============")
      print("You have encountered a river")
      river_encountered = True
      user_choice = str(input("Would you like to swim or ford the river, or wait(cross,swim,wait)"))

      if (user_choice == "ford" or user_choice =="Ford" or user_choice =="frd"):
        frd_random = randrange(0,6,1)
        if frd_random ==0:
          print("You cross the river and lose no supplies")
        elif frd_random ==1:
          print("You ford the river but lose 1 Water")
          water_amnt = water_amnt-1
          print("You have",water_amnt,"Left")
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
          print("You have",animal_amnt,"left")
      elif (user_choice == "swim" or user_choice == "Swim" or user_choice == "swm"):
        swm_random = randrange(0,2,1)
          
        if swm_random == 0:
          print("You cross the river")
        else:
          print(name,"Drowned")
          print( name,"has died!")
          print("Game Over!")
          print("===============")
          alive = False
      elif (user_choice == "wait" or user_choice =="Wait" or user_choice == "wt"):
        print("*****WAITING*****")
        time.sleep(5)
        animal_amnt = animal_amnt - 2

        print("While you waited, 2 animals died")
        print("You have",animal_amnt,animal,"Left")

        



         


def end_game():
  print("You have completed your journey")
  
def main():
  #END
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive
  
  print("Welcome to Python Trail")         #Running different functions, Main body
  get_name()
  get_age()
  game_varsetup()
  start_game()
  if alive == True:
    end_game()

global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, medicine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice,alive
main()







