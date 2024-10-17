number = int(input("Enter a number: "))
prime_number = True
for i in range(2, number):
    if number % i == 0:
        prime_number = False
        break
if prime_number:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")