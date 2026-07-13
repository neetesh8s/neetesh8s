import random

def get_Choice():
    #This function will return the player's choice of Rock, Paper, or Scissors
    #Below is the code that has been edited to allow user input for the player's choice
    Player_Choice = input("Enter your choice (Rock, Paper, or Scissors): ") 
    #This is a list of options for the computer to choose from
    Options=["Rock", "Paper", "Scissors"] 
    Computer_Choice = random.choice(Options)
    ##This is a dictionary that stores the player's choice and the computer's choice
    Choices = {"Player": Player_Choice, "Computer": Computer_Choice} 
    return Choices

Choices=get_Choice()
print(Choices)
print()