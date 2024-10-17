def get_name():
    return input("Enter your name: ")
name = get_name()
names = set()

while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
        name = get_name()
for name in names:
    print(name)