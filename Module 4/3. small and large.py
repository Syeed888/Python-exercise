user = input("Enter a number: ")
number = int(user)
smallest = number
largest = number

while True:
    value = input("Enter a value: ")
    if value == "":
        break
    number = int(value)

    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
print("The smallest number is " + str(smallest))
print("The largest number is " + str(largest))


