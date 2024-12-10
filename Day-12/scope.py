# modifying global scope

enemies = 1 

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")



#local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# global scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()