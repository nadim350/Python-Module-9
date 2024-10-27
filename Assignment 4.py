import random

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

    def show_info(self):
        print(f"{self.registration_number:<10} {self.maximum_speed:<15} {self.current_speed:<15} {self.travelled_distance:<15}")

def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = random.randint(100, 200)
        cars.append(Car(registration_number, maximum_speed))

    race_ongoing = True
    while race_ongoing:
        for car in cars:
            change_speed = random.randint(-10, 15)
            car.accelerate(change_speed)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_ongoing = False
                break

    print(f"{'Registration':<10} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<15} {'Travelled Distance (km)':<15}")
    print("-" * 60)
    for car in cars:
        car.show_info()

if __name__ == "__main__":
    main()
