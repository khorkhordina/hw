from hw_2.base import Vehicle
from hw_2.engine import Engine
from hw_2.exceptions import NotEnoughFuel


class Car(Vehicle):
    def __init__(self, weight, started, fuel, fuel_consumption, engine=None):
        super().__init__(weight, started, fuel, fuel_consumption)
        self._engine = engine

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self._engine = engine



