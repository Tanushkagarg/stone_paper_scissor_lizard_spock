# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(choices)

def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == "rock" and opponent_choice in ["scissors", "lizard"]) or
        (user_choice == "paper" and opponent_choice in ["rock", "spock"]) or
        (user_choice == "scissors" and opponent_choice in ["paper", "lizard"]) or
        (user_choice == "lizard" and opponent_choice in ["paper", "spock"]) or
        (user_choice == "spock" and opponent_choice in ["rock", "scissors"])
    ):
        return f"\033[1m{user_choice.capitalize()} wins!\033[0m", 1
    else:
        return f"\033[1m{opponent_choice.capitalize()} wins!\033[0m", -1

def play_with_computer(player_name):
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input(f"{player_name}, enter your choice (rock, paper, scissors, lizard, spock) or 'quit' to exit: ").lower()

        if user_choice == "quit":
            print("Thanks for playing!")
            print(f"{player_name} Score: {user_score}\nComputer Score: {computer_score}")

            if user_score > computer_score:
                print(f"\033[1m{player_name} is the winner!\033[0m")
            elif user_score < computer_score:
                print("\033[1mComputer is the winner!\033[0m")
            else:
                print("It's a tie!")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                print("\nStarting a new game...")
                break
            else:
                return

        if user_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\n{player_name} chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result, score = determine_winner(user_choice, computer_choice)
        user_score += score
        computer_score -= score

        print(result)
        print(f"{player_name} Score: {user_score}\nComputer Score: {computer_score}\n")

def play_multiplayer():
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")

    player1_score = 0
    player2_score = 0

    while True:
        player1_choice = input(f"{player1_name}, enter your choice (rock, paper, scissors, lizard, spock) or 'quit' to exit: ").lower()

        if player1_choice == "quit":
            print("Thanks for playing!")
            print(f"{player1_name} Score: {player1_score}\n{player2_name} Score: {player2_score}")

            if player1_score > player2_score:
                print(f"\033[1m{player1_name} is the winner!\033[0m")
            elif player1_score < player2_score:
                print(f"\033[1m{player2_name} is the winner!\033[0m")
            else:
                print("It's a tie!")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                print("\nStarting a new game...")
                break
            else:
                return

        if player1_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
            print("Invalid choice. Please try again.")
            continue

        player2_choice = input(f"{player2_name}, enter your choice (rock, paper, scissors, lizard, spock) or 'quit' to exit: ").lower()

        if player2_choice == "quit":
            print("Thanks for playing!")
            print(f"{player1_name} Score: {player1_score}\n{player2_name} Score: {player2_score}")

            if player1_score > player2_score:
                print(f"\033[1m{player1_name} is the winner!\033[0m")
            elif player1_score < player2_score:
                print(f"\033[1m{player2_name} is the winner!\033[0m")
            else:
                print("It's a tie!")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                print("\nStarting a new game...")
                break
            else:
                return

        if player2_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
            print("Invalid choice. Please try again.")
            continue

        print(f"\n{player1_name} chose: {player1_choice}")
        print(f"{player2_name} chose: {player2_choice}")

        result1, score1 = determine_winner(player1_choice, player2_choice)
        result2, score2 = determine_winner(player2_choice, player1_choice)
        player1_score += score1
        player2_score += score2

        print(result1)
        print(f"{player1_name} Score: {player1_score}\n{player2_name} Score: {player2_score}\n")

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors Lizard Spock!")
    while True:
        print("Choose an option:")
        print("1. Play against the computer")
        print("2. Play with another player")

        option = input("Enter the option number (1 or 2): ")
        if option == "1":
            player_name = input("Enter your name: ")
            play_with_computer(player_name)
        elif option == "2":
            play_multiplayer()
        else:
            print("Invalid option. Please try again.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            print("\nStarting a new game...")
        else:
            break
