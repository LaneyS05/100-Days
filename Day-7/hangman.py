import random
import hangman_words
print("hANGMAN")

#word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)

#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"{lives}/6 LIVES LEFT")
    guess = input("guess a letter: ").lower()

    if guess in correct_letters:
        print(f"you already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess} that is not in the word. you lose a life")
        if lives == 0:
            game_over = True
            print("you loose")
            print(f"the word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("you win")

