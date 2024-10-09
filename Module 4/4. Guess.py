import random
number = random.randint(1, 10)
while True:
    user_input = int(input("Guess a number: "))
    if user_input == number:
        print("Correct number.")
        break
    elif user_input < number:
        print("Too low.")
    elif user_input > number:
        print("Too high.")