class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f"Color: {self.color}, "
                f"Passenger Seats: {self.count_passenger_seats}, "
                f"Baby Seat: {self.is_baby_seat}, "
                f"Is Busy: {self.is_busy}")


car = Car("black", 4, True)
car1 = Car("red", 2, False)
car2 = Car("pink", 4, True)
car_list = [car2, car1, car]


class Taxi:
    def __init__(self, cars: list):
        if all(isinstance(obj, Car) for obj in cars):
            self.cars = cars
        else:
            raise ValueError('некорректный тип данных')

    def find_car(self, count_passenger: int, is_baby: bool):
        find_car = []
        for car in self.cars:
            if count_passenger == car.count_passenger_seats and is_baby == car.is_baby_seat and not car.is_busy:
                car.is_busy = True
                find_car.append(str(car))
        if find_car:
            return f"Вашему запросу соответсвует: {find_car}"
        else:
            return None


car_in_taxi = Taxi(car_list)
print(car_in_taxi.find_car(2, False))
