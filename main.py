from random import randrange    #Import random

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
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, mediciine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice
  dollars = 400


  print("You have $400 dollars to spend")
  amnt_food = int(input("Please enter the amount of food you wish to have(food costs $10 per pound):"))
  print("You have chosen to buy", amnt_food,"Pounds of food")
  dollars = dollars-amnt_food * 10
  print("You have,",dollars,"dollars remaining")
  amnt_water = int(input("Please enter the amount of water you wish to carry(Water 1 Dollar per gallon):"))
  print("You purchased:",amnt_water,"Water")
  dollars = dollars-amnt_water * 2
  print("You have,",dollars,"dollars remaining")
  animal = ("Please enter the animal you would like to pull your wagon:")
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
  global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, mediciine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice
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
    random_action = randrange(1,21,1)
    distance_traveled = 0                   #How far you went
    distance_traveled = randrange(1,21,1)
    wagon_dist_traveled = wagon_dist_traveled + distance_traveled
    print("You have Traveled",wagon_dist_traveled)
    print("You traveled,", distance_traveled,"Miles Today")
    
    if random_action ==1:
      cholera = True
      print( name,"has contracted Cholera")
      user_choice = ""
      user_choice = str(input("Would you like to use medicine or continue(Type medicine or Continue)"))
      if (user_choice == "medicine" or user_choice == "med" or user_choice == "Medicine") :
        print("You are Cured!")
        cholera = False
      else:
        print( name,"has died!")
        print("Game Over!")
        print("===============")
        alive = False
    if random_action == 2:
      wagon_broken = True
      print("Your Wagon has broken down")
      user_choice = str(input("Would you like to use spare parts or continue?(Spare or Continue"))
      if (user_choice == "Spare" or user_choice == "spare" or user_choice == "spr"):
        wagon_broken = False
        print("Your Wagon is Repaired")
      else: 
        amnt_food = amnt_food - 2
        print("You lose 2 food from wild animals")
        print("You have:",amnt_food,"food left")
    if random_action == 4:
      python_encountered = True
      print("You have encountered a python")
      



  print("===============")    
  print("You have completed your journey!")

      
    

  


  
def main():
  #END
  
  print("Welcome to Python Trail")         #Running different functions, Main body
  get_name()
  get_age()
  game_varsetup()
  start_game()

global name, amnt_food, dollars, amnt_water, animal, animal_amnt, spareprts_amnt, mediciine_amnt, age, total_distance , distance_traveled, wagon_dist_traveled, random_action, user_choice
main()







