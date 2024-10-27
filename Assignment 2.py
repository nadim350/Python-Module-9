class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        new_speed = self.current_speed + change_speed
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def show_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.maximum_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

def main():
    my_car = Car("ABC-123", 142)

    for change in [30, 70, 50]:
        my_car.accelerate(change)
        print(f"Speed after accelerating by {change} km/h: {my_car.current_speed} km/h")

    my_car.accelerate(-200)
    print(f"Speed after emergency brake: {my_car.current_speed} km/h")

if __name__ == "__main__":
    main()
