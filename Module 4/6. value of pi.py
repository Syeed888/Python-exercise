import random
points = 100000
counter = 0
points_in_circles = 0
while counter < points:
    counter = counter + 1
    x = random.randint(-1000, 1000)/ 1000
    y = random.randint(-1000, 1000)/ 1000
    if x**2 + y**2 < 1:
        points_in_circles = points_in_circles + 1
print(f"Pi = {(points_in_circles / points) * 4} ")