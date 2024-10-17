def even_values(values):
    even_values = []
    for value in values:
        if value % 2 == 0:
            even_values.append(value)
    return even_values

values = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break;
    value = int(user_input)
    values.append(value)
print(f"Original list: {values}")
print(f"Even value list: {even_values(values)}")
