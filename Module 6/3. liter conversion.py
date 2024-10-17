
gallon_liters = 3.785
def gallons_to_liters(gallons):
    return gallons * gallon_liters

while True:
    gallons = input("Gallons: ")

    if gallons == "":
        break;
    if float(gallons) < 0:
        break;

    print(gallons_to_liters(float(gallons)))