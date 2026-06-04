import time 
import gradio
pet_name = input("What is your pet's name? ")
hunger = 5 
happiness = 5 
def hhprint():
    print(f"Hunger: {hunger}")
    print(f"Happiness: {happiness}")

while True:
    def limits():
     global hunger, happiness
     if hunger >10:
      hunger = 10
     if hunger <0:
        hunger = 0
     if happiness<0:
       happiness = 0
     if happiness>10:
       happiness = 10
    
    print(f"\n---{pet_name}---")
    hhprint()
    print("\n1.Feed Pet")
    print("2. Play with pet")
    print("3. Check Status")
    print("4.Exit")
    print("5.give rest and food")
    userchoice = int(input("Choose an option "))
    if userchoice == 1:
      hunger -= 2
      limits()
      print(f"{pet_name} is eating!")
      hhprint()
    elif userchoice == 2:
       happiness += 2
       hunger -= 1
       hhprint()
       print(f"You played with, {pet_name}")
    elif userchoice == 3:
       print(f"---status report---")
       limits()
       hhprint()
    elif userchoice == 4:
       print("Goodbye")
       break
    elif userchoice == 5:
       happiness += 3
       hunger -= 3
       limits() 
       print(f"{pet_name}, is resting, rest is important.")
    else:
       print("Sorry Invalid choice, Try these-")
       print("\n1.Feed Pet")
       print("2. Play with pet")
       print("3. Check Status")
       print("4.Exit")
       print("5.rest and give food")
    hunger +=1
    happiness -=1
    limits()
    if hunger == 10:
      print("Oh! no your pet is very hungry he wont be as happy now")
      happiness -=4
    if happiness == 0:
       print("OH! no you pet is unhappy!")
    time.sleep(1)
       
       
       
       
    
"""
health meter
cleanliness meter
game loss if hunger is 10 or happiness is 0

"""