import random
from config import GAME_CHOICES, RULES

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


def play():

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
            print("Drow")

    print(f'User: {result["User"]} System: {result["System"]}')
            

if __name__ == "__main__":
    play()