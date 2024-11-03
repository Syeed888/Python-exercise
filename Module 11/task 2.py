import random

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.speed = random.randint(80, max_speed)
        self.distance_driven = 0

    def drive(self):
        speed_change = random.randint(-10, 10)
        self.speed += speed_change
        self.speed = max(0, self.speed)
        self.distance_driven += self.speed


class ElectricCar(Car):
    def __init__(self, name, max_speed, battery_capacity):
        super().__init__(name, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, name, max_speed, tank_volume):
        super().__init__(name, max_speed)
        self.tank_volume = tank_volume


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    for i in range(3):
        electric_car.drive()
        gasoline_car.drive()

    print(f"Electric Car ({electric_car.name}): {electric_car.distance_driven} km driven")
    print(f"Gasoline Car ({gasoline_car.name}): {gasoline_car.distance_driven} km driven")


main()
