from elevator import Elevator

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom_floor = bottom
        self.top_floor = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number")
            return
        print(f"Running elevator {elevator_number} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        for i in range(len(self.elevators)):
            print(f"Moving elevator {i} to the bottom floor.")
            self.elevators[i].go_to_floor(self.elevators[i].bottom_floor)