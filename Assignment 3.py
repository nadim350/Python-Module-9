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

    def drive(self, hours):
        if self.current_speed > 0:
            distance_covered = self.current_speed * hours
            self.travelled_distance += distance_covered
            print(f"Driving for {hours} hours at {self.current_speed} km/h covers {distance_covered} km.")
        else:
            print("The car is not moving, so no distance is covered.")

    def show_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.maximum_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

def main():
    my_car = Car("ABC-123", 142)

    my_car.accelerate(30)
    print(f"Speed after accelerating by 30 km/h: {my_car.current_speed} km/h")
    my_car.accelerate(70)
    print(f"Speed after accelerating by 70 km/h: {my_car.current_speed} km/h")
    my_car.accelerate(50)
    print(f"Speed after accelerating by 50 km/h: {my_car.current_speed} km/h")

    my_car.accelerate(-200)
    print(f"Speed after emergency brake: {my_car.current_speed} km/h")

    my_car.accelerate(60)
    my_car.drive(1.5)
    print(f"Travelled distance after driving for 1.5 hours: {my_car.travelled_distance} km")

    my_car.show_info()

if __name__ == "__main__":
    main()
