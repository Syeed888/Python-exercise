import random
roll = int(input("Enter a number: "))
total = 0
for i in range(roll):
    total = total + random.randint(1,6)
print(total)