from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_FUEL = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity / (self.fuel_consumption + self.AC_FUEL) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_FUEL)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_FUEL = 1.6
    REFUEL_PERCENT = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity / (self.fuel_consumption + self.AC_FUEL) >= distance:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_FUEL)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.REFUEL_PERCENT



# TEST CODE:

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)