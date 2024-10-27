import random

class car:
    def __init__(self, name):
        self.name = name
        self.speed = random.randint(80, 120)
        self.distance_driven = 0

    def drive(self):
        speed_change = random.randint(-10, 10)
        self.speed += speed_change
        self.speed = max(0, self.speed)
        self.distance_driven += self.speed

