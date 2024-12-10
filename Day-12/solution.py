from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high")
        return turns -1

    elif user_guess < actual_answer:
        print("too low")
        return turns -1
        
    else:
        print("you win")

def set_difficulty():
    level = input("choose a difficulty. type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL



def game():
    print("im thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"{answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} guesses left")
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you ran out of tries")
            return

game()