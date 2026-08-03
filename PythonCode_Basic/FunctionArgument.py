import random
def get_Choice() :
    Player_Choice = input("Enter player choice(Rock, Paper or Scissor): ")
    #Computer_Choice = "Scissor"
    Options = ["Rock", "Paper", "Scissor"]
    Computer_Choice = random.choice(Options)
    Choice = {"Player":Player_Choice, "Computer":Computer_Choice}
    return Choice

def Check_Win() :
    print