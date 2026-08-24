import random
def roll_dice(sides):
    roll = random.randint(1 , sides)
    return roll
roll_result = None
sides_input = int(input("Syötä tahkojen määrä: "))
while roll_result!=sides_input:
    roll_result = roll_dice(sides_input)
    print(roll_result)