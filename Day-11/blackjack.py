import random

def blackjack():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        your_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)

        player_score = sum(your_cards)
        computer_score = sum(computer_cards)
        print(f"Your cards: {your_cards} current player_score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 21 and len(your_cards) == 2:
            print("You win! Blackjack!")
            return
        elif computer_score == 21 and len(computer_cards) == 2:
            print("Computer wins! Blackjack!")
            return

        while True:
            get_another_card = input("'y' to get another card 'n' to pass: ")

            if get_another_card == 'y':
                new_player_card = random.choice(cards)
                your_cards.append(new_player_card)
                player_score = sum(your_cards)
                print(f"Your cards: {your_cards} current player score: {player_score}")

                if player_score > 21:
                    print("You lost, bust!")
                    return
            elif get_another_card == 'n':
                print(f"Your final cards: {your_cards}, final score: {player_score}")
                break
            else:
                print("Invalid input. Please type 'y' or 'n'.")

        print(f"Computer's final cards: {computer_cards}, current score: {computer_score}")
        while computer_score < 17:
            new_computer_card = random.choice(cards)
            computer_cards.append(new_computer_card)
            computer_score = sum(computer_cards)
            print(f"Computer drew a card. New computer score: {computer_score}")

            if computer_score > 21:
                print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
                print("You win! The computer went bust!")
                return

        print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
        if player_score > computer_score:
            print(f"You win! Your score: {player_score}, Computer score: {computer_score}")
        elif computer_score > player_score:
            print(f"You lose. Your score: {player_score}, Computer score: {computer_score}")
        else:
            print(f"It's a tie! Your score: {player_score}, Computer score: {computer_score}")
    else:
        print("Maybe next time!")

blackjack()
