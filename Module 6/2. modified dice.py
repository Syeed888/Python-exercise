import random
def random_dice_roll(max):
    return random.randint(1, max)
max_side = input("Number of sides: ")

if max_side == "":
    max_side = 6
else:
    max_side = int(max_side)

while True:
    roll = random_dice_roll(max_side)
    print(f"Roll: {roll}")
    if roll == 6:
        break;