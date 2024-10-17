def sum(values):
    total = 0
    for value in values:
        total = total + value
    return total
values = []
while True:
    inputs = input("Enter a number: ")
    if inputs == "":
        break;
    value = int(inputs)
    values.append(value)
print(sum(values))