import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors) : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    choices = {"player": player_choice, "computer": computer_choice}
    
    return check_win(player_choice, computer_choice)

def check_win(player, computer):
    print(f"You chose {player}, and the computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"
        
choices = get_choices()
        
print(choices)