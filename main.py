import random
from config import GAME_CHOICES, RULES, scoreboard
from datetime import datetime
from decorators import log_time

def get_user_choice():

    user_input = input("Please, enter your choice (r, p, s): ")
    if user_input not in GAME_CHOICES:
        print("Wrong choice. Please try again.")
        return get_user_choice()
    
    return user_input

def get_system_choice():
    return random.choice(GAME_CHOICES)

def find_winner(user, system):

    match = {user, system}

    if len(match) == 1:
        return None
    
    sort_match = sorted(match)
    t_match = tuple(sort_match)
    
    return RULES[t_match]


def update_scoreboard(result):
    if result["User"] == 3:
        scoreboard["User"] += 1
        msg = "You won."
    elif result["System"] == 3:
        scoreboard["System"] += 1
        msg = "You lost."

    show_result(msg)

def show_result(msg):
    print("#" * 29)
    print("##" f' User: {scoreboard["User"]}'.ljust(26), "##")
    print("##" f' System: {scoreboard["System"]}'.ljust(26), "##")
    print("##" f' Last game: {msg}'.ljust(26), "##")
    print("#" * 29)

def play_game():

    result = {"User": 0, "System": 0}

    while result["User"] < 3 and result["System"] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        print(f"User choice: {user_choice} \t System choice: {system_choice}")

        if winner == user_choice:
            result["User"] += 1
            print("User won.")

        elif winner == system_choice:
            result["System"] += 1
            print("System won.")

        else:
            print("Draw")
    
    update_scoreboard(result)
    play_again()

def play_again():
    user_response = input("Do you want to play again? (Yes/No) ").capitalize()
    if user_response == "Yes":
        play_game()
    elif user_response == "No":
        print("Game ended. Thanks for playing.")
        return
    else:
        print("Failed. Please just enter yes or no.")
        return play_again()

@log_time  
def play():
    play_game()

if __name__ == "__main__":
    play()