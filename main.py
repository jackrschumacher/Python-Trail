from random import randrange    #Import random

def name():        
  name = str(input("What is your name?"))
  print("Your name is,",name)

def age():
  age = str(input("Please enter your age:"))
  print("Your age is:",age)
  

#END

def game_varsetup():     #Buy Supplies
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




def start_game(location_start):
  
  print("LOADING...")
  print("===============")
  print("You begin in Wisconsin and Travel to Flordia)
  total_distance = 0
  total_distance = randrange(500,20001,1)
  distance_traveled = 0

  if total_distance <= distance_traveled:
    distance_traveled = randrange(1,20,1)
    print("You traveled",distance_traveled,"Miles")
  


  
  
def main():
  #END
  
  print("Welcome to Python Trail")         #Running different functions, Main body
  name()
  age()
  location_start()
  location_end()
  game_varsetup()
  start_game(location_start)


main()







