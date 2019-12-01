# Assign even numbers to Bob and odd numbers to Alice
def Winner(stone_number):
    if stone_number%2==0:
        return "Bob"
    else:
        return "Alice"
print(Winner(int(input())))