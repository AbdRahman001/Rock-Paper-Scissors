import random

choices = ['R', 'P', 'S']

while True:
    user_choice = input("Enter a choice (R, P, S): ")
    possible_choice = ["R", "P", "S"]
    computer_choice = random.choice(possible_choice)

    print(f"\n You chose {user_choice}, computer chose {computer_choice} \n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. A Tie!")
    elif user_choice == "R":
        if computer_choice == "S":
            print("Rock smashes scissors! YOU WIN")
        else:
            print ("Paper covers Rock! YOU LOSE")
    elif user_choice == "P":
        if computer_choice == "R":
            print("Paper covers Rock, YOU WIN")
        else:
            print("Scissors cuts paper! YOU LOSE")
    elif user_choice == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! YOU WIN")
        else:
            print("Rock smashes scissors! YOU LOSE")
play_again = input("Do you want to play again? (y/n): ")
