import random

rock = "rock"
paper = "paper"
scissors = "scissors"

game_strings = [rock, paper, scissors]

player_num = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))
if player_num >= 0 and player_num <= 2:
    print(game_strings[player_num])

computer_num = random.randint(0, 2)
print("the computer chose: ")
print(game_strings[computer_num])

if player_num == 0 and computer_num == 2:
    print("you win")
elif player_num >= 3 or player_num < 0:
    print("you lose")
elif computer_num == 0 and player_num == 2:
    print("you lose")
elif computer_num > player_num:
    print("you lose")
elif player_num > computer_num:
    print("you win")
elif computer_num == player_num:
    print("its a draw")

