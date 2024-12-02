name = input("type your name: ")

def greet(name):
    print(f"hello {name}")
    print("hi")
    print("hey")

greet(name)

# more than one input 

def greet_with(name, location):
    print(f"{name} from {location}")

greet_with(location="SC", name="Laney")