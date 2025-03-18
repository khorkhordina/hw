from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, started, fuel, fuel_consumption, cargo=0, max_cargo=0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self._cargo = cargo
        self._max_cargo = max_cargo

    @property
    def cargo(self) -> float:
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if value < 0:
            raise ValueError
        if value > self._max_cargo:
            raise CargoOverload()
        self._cargo = value

    @property
    def max_cargo(self):
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, value):
        if value < 0:
            raise ValueError
        self._max_cargo = value


    def load_cargo(self, amount):
        if self.cargo + amount <= self._max_cargo:
            self._cargo += amount
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        previous_cargo = self._cargo
        self._cargo = 0
        return previous_cargo




