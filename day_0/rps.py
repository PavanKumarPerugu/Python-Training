import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}

    return choices

def check_win(player,computer):
    print(f"Player opted choice is {player} and Computer opted choice is {computer}")

    if player == computer:
        return "It's a Tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers Rock! You lose!"
        else:
            return "Rock smashes Scissors! You win!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts Paper! You lose!"
        else:
            return "Paper covers Rock! You win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes Scissors! You lose!"
        else:
            return "Scissors cuts Paper! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)