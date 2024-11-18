print("welcome to treasure island")

left_or_right = input('you\'re at a crossroad, where do you want to go?' 
'type left or right? ').lower()


if left_or_right == "left":
    swim_or_wait = input('you\'ve have come to a lake there is an island in the middle of the lake.' 
    'swim or wait on boat. type swim or wait:  ').lower()
    if swim_or_wait == "wait":
        which_door = input('there are 3 doors on the island pick a door blue, yellow or red ').lower()
        if which_door == "yellow":
            print("YOU WIN")
        elif which_door == "red":
            print("burned by fire")
            print("GAME OVER")
        elif which_door == "blue":
            print("eaten by the beasts")
            print("GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("attacked by trout")
        print("GAME OVER")
else:
    print("you fell in a hole")
    print("GAME OVER")