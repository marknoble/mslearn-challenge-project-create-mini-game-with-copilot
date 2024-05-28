# This application is a "rock, paper, scissors" minigame.
# The user will be prompted to enter their choice of rock, paper, or scissors and must be warned if they enter an invalid option.
# The computer will randomly select one of the three options and the winner will be determined based on the rules of the game.
# The user will be prompted to play again or exit the game after each round.
# The user will be able to see the number of rounds they have played and the number of rounds they have won, lost, or tied.

# Lets start by prompting the user to enter their choice of rock, paper, or scissors.
# This will be done in a while loop that will run as long as the user wants to play the game.
# We will also initialize variables to keep track of the number of rounds played, the number of rounds won, the number of rounds lost, and the number of rounds tied.
# The user will be prompted to enter their choice of rock, paper, or scissors and the computer will randomly select one of the three options.
# The winner will be determined based on the rules of the game and the user will be prompted to play again or exit the game.
# The user inputs must be put in lowercase to avoid case sensitivity issues and the user must be warned if they enter an invalid option.

import random

rounds_played = 0
rounds_won = 0
rounds_lost = 0
rounds_tied = 0

while True:
    print("\nRock, Paper, Scissors\n")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        rounds_tied += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        rounds_won += 1
    else:
        print("You lose!")
        rounds_lost += 1

    rounds_played += 1

    print("\nRound Summary")
    print(f"Rounds played: {rounds_played}")
    print(f"Rounds won: {rounds_won}")
    print(f"Rounds lost: {rounds_lost}")
    print(f"Rounds tied: {rounds_tied}")

    play_again = input("\nDo you want to play again? (yes or no): ").lower()
    if play_again != "yes":
        break

print("\nThanks for playing!")