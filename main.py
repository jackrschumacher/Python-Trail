from random import randrange

def intro():
  name = str(input("What is your name?"))
  print("Your name is,",name)
  age = str(input("Please enter your age:"))
  print("Your age is:",age)
  location_start = str(input("Where would you like to start your adventure from?"))
  print("You have chosen to start in:",location_start)
  location_end = str(input("Where would you like your adventure to end?"))
  print("You have chosen to end at:",location_end)

def game_varsetup():
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
  animal_amnt = int(input("Please enter the number of animals you wish to pull your wagon (animals are 15 per animal): "))  
  print("You purchased:",animal_amnt,"Animals")
  dollars = dollars-animal_amnt
  print("You have:",dollars,"Dollars Remaining")



print("Welcome to Python Trail")
intro()
game_varsetup()







