size = input("what size pizza do you want? S, M or L: ")
pepperoni = input("do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
    print("$15 for small")
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1

elif size == "M":
    bill = 20
    print("$20 for medium")
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    print("$25 for large")
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(bill)
