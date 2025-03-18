### Домашнее задание "Классы"

1.Добавлены и реализованы исключения в hw_2.exceptions:
LowFuelError
NotEnoughFuel
CargoOverload

2.Доработан базовый класс hw_2.base.Vehicle:
Добавлены атрибуты weight, started, fuel, fuel_consumption
Реализован __init__ с установкой значений
Метод start() проверяет состояние started, наличие топлива и обновляет статус
Метод move(distance) проверяет, достаточно ли топлива, и уменьшает его количество

3.Создан датакласс Engine в hw_2.engine:
Атрибуты volume и pistons

4.Создан класс Car в hw_2.car:
Добавлен атрибут engine
Реализован метод set_engine(engine: Engine)

5.Создан класс Plane в hw_2.plane:
Добавлены атрибуты cargo и max_cargo
Метод load_cargo(value) добавляет груз, проверяя на перегруз
Метод remove_all_cargo() возвращает загруженный вес и обнуляет cargo

