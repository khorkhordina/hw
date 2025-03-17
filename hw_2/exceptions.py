class LowFuelError(Exception):
    def __init__(self, message="Топливный бак пуст. Запуск невозможен"):
        super().__init__(message)


class NotEnoughFuel(Exception):
    def __init__(self, message="Не достаточно топлива для поездки, нужно заправиться"):
        super().__init__(message)


class CargoOverload(Exception):
    def __init__(self, message="Перегруз, уменьшите вес груза"):
        super().__init__(message)
