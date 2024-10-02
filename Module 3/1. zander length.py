length = float(input("Enter zander length in centimeters: "))
minimum_length = 42
if length < minimum_length:
    print("This is undersize and it needs to be " + str(minimum_length - length) + " cm longer")
else:
    print("This is ok")