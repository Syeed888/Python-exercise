import math
def pizza_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return price / (area / 1000)
print("Pizza 1 ")
pizza1_diameter = float(input("Pizza 1 diameter in cm: "))
pizza1_price = float(input("Pizza 1 price in euro: "))

print("Pizza 2 ")
pizza2_diameter = float(input("Pizza 2 diameter in cm: "))
pizza2_price = float(input("Pizza 2 price in euro: "))

pizza1_price = pizza_price(pizza1_diameter, pizza1_price)
pizza2_price = pizza_price(pizza2_diameter, pizza2_price)

print(f"Pizza 1 price: {pizza1_price: <.2f}")
print(f"Pizza 2 price: {pizza2_price: <.2f}")

if pizza1_price < pizza2_price:
    print("Pizza 1 gives best values")
else:
    print("Pizza 2 gives best values")