from Race import race
from Car import car

if __name__ == "__main__":
    car_list = [car(f"Car {i + 1}") for i in range(10)]

    race1 = race("Grand Demolition Derby", 8000, car_list)

    hours_passed = 0

    while not race1.race_finished():
        race1.hour_passes()
        hours_passed = hours_passed + 1

        if hours_passed % 10 == 0:
            race1.print_status()

    print("Race finished!")
    race1.print_status()
