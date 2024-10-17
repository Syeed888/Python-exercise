import random
def random_roll():
    return random.randint(1,6)
while True:
    roll = random_roll()
    print(f"Roll is: {roll}")
    if roll == 6:
        break;