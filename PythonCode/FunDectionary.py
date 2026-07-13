def get_Choice():
    #This function will return the player's choice of Rock, Paper, or Scissors
    #Below is the code that has been edited to allow user input for the player's choice
    Player_Choice = input("Enter your choice (Rock, Paper, or Scissors): ") 
    Computer_Choice = "Scissors" #This is Variable assign to Computer_Choice
    ##This is a dictionary that stores the player's choice and the computer's choice
    Choices = {"Player": Player_Choice, "Computer": Computer_Choice} 
    return Choices

Choices=get_Choice()
print(Choices)
#creating disctionary using dict() function
d=dict({1:"Rock", 2:"paper", 3:"scissors"})
print(d)
print(d.get(1))