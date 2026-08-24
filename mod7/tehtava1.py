import random
def roll_dice():
    roll = random.randint(1 , 6)
    return roll
roll_result = None
while roll_result!=6:
    roll_result = roll_dice()
    print(roll_result)