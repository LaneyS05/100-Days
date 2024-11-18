height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride")
    age = int(input("how old are you? "))
    if age <= 12:
        print("child tickets are $5")
        bill = 5
    elif age <= 18:
        print("youth tickets are $7")
        bill = 7
    elif age <= 45 or age >= 55:
        print("your ticket is free")
    else:
        print("adult tickets are $12")
        bill = 12 
    
    photo = input("do you want a photo? type y for yes and n for no: ") 
    if photo == "y":
        bill += 3
        print(f"your total is {bill}")
else:
    print("your to small")
