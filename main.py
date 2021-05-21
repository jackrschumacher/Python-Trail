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


  print("You have",dollars, "dollars to spend")
  amnt_food = int(input("Please enter the amount of food you wish to have(food costs $10 per pound):"))
  print("You have chosen to buy", amnt_food,"Pounds of food")
  dollars = dollars-amnt_food * 10
  print("You have,",dollars,"dollars remaining")
  amnt_water = int(input("Please enter the amount of water you wish to carry(Water 1 Dollar per gallon):"))
  print("You purchased:",amnt_water,"Water")
  dollars = dollars-amnt_water * 2
  print("You have,",dollars,"dollars remaining")
  animal = str(input("Please enter the animal you would like to pull your wagon:"))
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
    print("You have Traveled:",wagon_dist_traveled,"In Total")
    print("You traveled,", distance_traveled,"Miles Today")
    
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
      else: 
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
          print("You capture the python")
          print("===============")
        elif hunt_random ==2:
          print("You capture the python, but it escapes")
          print("===============")
      else:
        print("The python comes back when you are sleeping and Kills one of your",animal)
        animal = animal-1
        print("You have:",animal_amnt,"left")
        print("===============")
    
    if random_action ==5:
      print("===============")
      town_encountered = True
      print("You have encountered a town!")
      user_choice = str(input("Would you like to continue or stop and buy Supplies (Continue or Stop)"))
      if (user_choice == "Stop" or user_choice =="Stop" or user_choice =="stp"):
        print("You have chosen to stop at the town")
        print("You can choose to buy additonal medicine, Animals, Water or Food")
        animals_add = int(input("Please enter how many animals you wish to buy:"))
        animal_amnt = animal_amnt+animals_add
        print("You have", animal_amnt,"Animals")
        add_med = int(input("How much medicine would you like to buy?:"))
        mediciine_amnt = mediciine_amnt+add_med
        print("You have",mediciine_amnt,"Medicine")
        add_water = int(input("How much water would you like to buy?:"))
        amnt_water = amnt_water+add_water
        print("You have:",amnt_water,"Water")
        add_food = int(input("Please enter how much food you wish to buy?:"))
        amnt_food = amnt_food + add_food
        print("You have",amnt_food,"Food")
        print("===============")
      else:
        print("You continue on")
        print("===============")



      



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







