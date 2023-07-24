import random

def get_choices():
    print("\n----- Welcome to the game! -----")
    print("oo-----oooooooooooooooooo-----oo\n")
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player.lower()}, computer chose {computer}\n")

    if player.lower() == computer:
        return "It's a tie!"

    elif player.lower() == "rock":
        if computer == "scissors":
            return "--- Rock smashes scissors! You win! ---"
        else:
            return "--- Paper covers rock! You lose! ---"

    elif player.lower() == "paper":
        if computer == "rock":
            return "--- Paper covers rock! You win! ---"
        else:
            return "--- Scissors cuts paper! You lose! ---"

    elif player.lower() == "scissors":
        if computer == "paper":
            return "--- Scissors cuts paper! You win! ---"
        else:
            return "--- Rock smashes scissors! You lose! ---"

    else:
        print("--- unidentified object chosen!! ---")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result + "\n")
print("----- Game Over -----\n")