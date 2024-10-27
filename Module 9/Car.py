class car:
    def __init__(self, reg_num, max_speeed, current =0, distance=0):
        self.registration_number = reg_num
        self.maximum_speed = max_speeed
        self.current_speed = current
        self.travelled_distance = distance

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)