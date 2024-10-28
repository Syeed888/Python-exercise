import random
from Car import car

def main():

    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car1 = car(f"ABC-{i}", max_speed)
        cars.append(car1)

    race_hours = 5
    for hour in range(race_hours):
        print(f"Hour {hour + 1}:")
        for car1 in cars:
            speed_change = random.randint(-10, 15)
            car1.accelerate(speed_change)
            car1.drive(1)
            print(f"{car1.registration_number}, Current Speed: {car1.current_speed}, Travelled Distance: {car1.travelled_distance}")
            if car1.travelled_distance >= 10000:
            print(f"{car1.registration_number}, Current Speed: {car1.current_speed}, Travelled Distance: {car1.travelled_distance}")
            break
if __name__ == "__main__":
    main()
