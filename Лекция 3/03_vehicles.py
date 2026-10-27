"""Практика 2 (слайд 34): полиморфизм транспортных средств."""


class Vehicle:
    def __init__(self, name, max_speed):
        if max_speed <= 0:
            raise ValueError(
                "Максимальная скорость должна быть положительной."
            )
        self.name = name
        self.max_speed = max_speed

    def description(self):
        return f"{self.name}, максимальная скорость {self.max_speed} км/ч"


class Car(Vehicle):
    def __init__(self, name, max_speed, fuel_type):
        super().__init__(name, max_speed)
        self.fuel_type = fuel_type

    def description(self):
        return f"Автомобиль {super().description()}, топливо: {self.fuel_type}"


class Bicycle(Vehicle):
    def __init__(self, name, max_speed, gears):
        super().__init__(name, max_speed)
        if type(gears) is not int or gears < 1:
            raise ValueError("У велосипеда должна быть хотя бы одна передача.")
        self.gears = gears

    def description(self):
        return f"Велосипед {super().description()}, передач: {self.gears}"


class Boat(Vehicle):
    def __init__(self, name, max_speed, capacity):
        super().__init__(name, max_speed)
        if type(capacity) is not int or capacity < 1:
            raise ValueError(
                "Вместимость должна быть положительным целым числом."
            )
        self.capacity = capacity

    def description(self):
        return f"Катер {super().description()}, мест: {self.capacity}"


if __name__ == "__main__":
    vehicles = [
        Vehicle("Транспорт", 20),
        Car("Лада", 180, "бензин"),
        Bicycle("Стелс", 35, 21),
        Boat("Волна", 60, 6),
    ]
    for vehicle in vehicles:
        print(vehicle.description())
