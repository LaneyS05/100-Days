bidding = True
my_dict = {}
while bidding:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    players = input("Are there any other bidders? Type yes or no: ").lower()

    my_dict[name] = bid
    print(my_dict)

    print("\n" * 20)

    if players == "yes":
        bidding = True
    elif players == "no":
        bidding = False
        break
    else:
        bidding = False
        print("error")
        break
max_key = max(my_dict, key=my_dict.get)
max_value = max(my_dict.values())
print(f"{str(max_key)} won with {str(max_value)}")
