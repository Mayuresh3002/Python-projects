import random

user_win = 0
computer_win = 0

option = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to Quit.: ").lower()
    if user_input == "q":
        break
    
    if user_input not in option:
        continue
    
    random_num = random.randint(0,2)
    # rock:0, paper=1, scissor:2

    computer_pick = option[random_num]
    print("computer picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("you won!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_win += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("you won!")
        user_win += 1

    else:
        print("you lost!")
        computer_win += 1

print("You won",user_win,"times.")
print("The computer won",computer_win,"times.")
print("Goodbye!")
