num = int(input("type a number: "))

is_even = num % 2 == 0

if is_even:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")


a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")