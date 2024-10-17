numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break;
    number = int(user_input)
    numbers.append(number)
numbers.sort(reverse=True)
print(numbers[:5])