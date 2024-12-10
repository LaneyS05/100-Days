# my game
import random

number = random.randint(1, 100)

# for testing
#print(number) 

print("im thinking of a number between 1 and 100")

difficulty = input("choose a difficulty. type 'easy' or 'hard': ")

def guess_number(number):
    hard_level = 5
    easy_level = 10
    has_guesses = True

    while has_guesses:
        if difficulty == "easy":
            print(f"you have {easy_level} guesses")
            player_guess = int(input("Make a guess: "))

            if player_guess > number:
                print("to high")
                print("guess again")
                

            if player_guess < number:
                print("to low")
                print("guess again")
            easy_level -= 1



        if difficulty == "hard":
            print(f"you have {hard_level} guesses")
            player_guess = int(input("Make a guess: "))

            if player_guess > number:
                print("to high")
                print("guess again")
                

            if player_guess < number:
                print("to low")
                print("guess again")
            
            hard_level -= 1
        
        if player_guess == number:
            print("you win")
            return 

        if hard_level == 0 or easy_level == 0:
            print("you ran out of guesses")
            print("you lose")
            has_guesses = False

guess_number(number)
