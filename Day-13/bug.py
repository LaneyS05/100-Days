def my_function():
    for i in range(1, 21):
        if i == 20:
            print("you got it")

my_function()

# reproduce the bug 

from random import randint
dice_images = ["1️⃣", "2️⃣","3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

# play computer

year = int(input("What is your year of birth: "))

if year > 1980 and year < 1994:
    print("you are a millennial")
elif year >= 1994:
    print("you are a gen z")

# fix the errors

try:
    age = int(input("How old are you? "))
except ValueError:
    print("please type a number")
    age = int(input("How old are you? "))
if age > 18:
    print(f"you can vote at {age}")

# print

#word_per_page = 0
pages = int(input("number of pages: "))
word_per_page = int(input("number of words per page: "))
total_words = pages * word_per_page

print(f"pages = {pages}")
print(f"words per page = {word_per_page}")
print(total_words)

# use a debuger
import random
import math

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = new_item + item
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])