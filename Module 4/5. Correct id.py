username = "python"
password = "rules"
guess = 0
while guess < 5:
    user_name = input("Enter name: ")
    pass_word = input("Enter password: ")
    if user_name == username and pass_word == password:
        print("Welcome")
        break
    guess = guess + 1
else:
    print("Access denied")