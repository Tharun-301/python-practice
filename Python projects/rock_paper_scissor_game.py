import random

def user_choice():
    while True:
        choice = input("Choose Rock (r) Paper (p) Scissors (s): ").lower()
        if choice in ['r', 'p', 's']:
            return choice
        else:
            print("Invalid choice! Please enter r, p, or s.")

def play():
    print("\n==== Rock Paper Scissors Game ====\n")

    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    user = user_choice()
    computer = random.choice(['r', 'p', 's'])
    print(f"You chose: {choices[user]}")
    print(f"Computer chose: {choices[computer]}")

    if user == computer:
        return "It's a tie!🤷"
    if (user == 'r' and computer == 's') or \
       (user == 's' and computer == 'p') or \
       (user == 'p' and computer == 'r'):
        return "You won!🎉"
    return "You lost!😞"

print(play())
