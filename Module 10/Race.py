import random
from Car import car

class race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.drive()

    def print_status(self):
        print(f"Race: {self.name}")
        print(f"Distance: {self.distance} ")
        print(f"{'Car Name':<15}{'Distance Driven (km)':<25}{'Current Speed (km/h)'}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.name:<15}{car.distance_driven:<25.2f}{car.speed:.2f}")


    def race_finished(self):
        for car in self.cars:
            if car.distance_driven >= self.distance:
                return True
        return False
