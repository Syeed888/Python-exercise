talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))
talents_pounds = 20
pounds_lots = 32
lots_gram = 13.3
lots_grams = lots * lots_gram
pounds_grams = pounds * pounds_lots * lots_gram
talents_grams = talents * talents_pounds * pounds_lots * lots_gram

mass = lots_grams + pounds_grams + talents_grams
kilograms = int(mass/1000)
grams = mass - (kilograms * 1000)
print("The weight in modern units: ")
print(str(kilograms) + " kilograms and " + str(grams) + " grams")
