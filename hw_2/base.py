from abc import ABC
from hw_2.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight=0, started=False, fuel=0.0, fuel_consumption=0.0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            raise ValueError("Двигатель запущен")
        if not self.started and self.fuel > 0:
            self.started = True
        elif self.fuel <= 0:
            raise LowFuelError()

    def move(self, distance):
        if not self.started:
            raise ValueError("Двигатель не запущен")
        required_fuel = distance * self.fuel_consumption / 100
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            return f"Вы проехали {distance} км. Осталось {self.fuel} топлива"
        else:
            raise NotEnoughFuel()















