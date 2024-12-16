import random
from game_data import game_data

def get_B(exclude):
    while True:
        random_B = random.choice(game_data)
        if random_B != exclude:
            return random_B
    
def compare():
    Score = 0

    random_A = random.choice(game_data)

    while True:
        random_B = get_B(random_A)


        follower_count_A = random_A["follower_count"]
        follower_count_B = random_B["follower_count"]

        print(f"Compare A: {random_A['name']} a {random_A['occupation']} who lives in {random_A['country']}")
        print(f"Against B: {random_B['name']} a {random_B['occupation']} who lives in {random_B['country']}")

        followers = input("Who has more followers? Type 'A' or 'B': ").upper()

        if followers == "A" and follower_count_A > follower_count_B:
            Score+= 1
            print(f"You're right. Current score: {Score}")

            if follower_count_A > follower_count_B:
                random_A = random_B

            while True:
                random_B = random.choice(game_data)
                if random_B != random_A:
                    break

            else:
                random_A, random_B = random_A, random_B

        elif followers == "B" and follower_count_B > follower_count_A:
            Score += 1
            print(f"You're right. Current score: {Score}")

            if follower_count_A > follower_count_B:
                random_A, random_B, random_B, random_A

            else: 
                random_A, random_B = random_A, random_B

        else:
            print(f"sorry, that's wrong. Final score: {Score}")
            return

compare()
#def game():
    