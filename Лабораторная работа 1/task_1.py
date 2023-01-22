import doctest

class Client:

    def __init__(self, capital: float, floor: int, expensive_room: int, cheap_room: int):
        if not isinstance(capital, (int, float)):
            raise TypeError("Капитал должен быть типа int или float")
        if capital <= 0:
            raise ValueError("Капитал должен быть положительным числом")
        self.capital = capital

        if not isinstance(floor, int):
            raise TypeError("Этаж должен быть типа int")
        if floor > 10:
            raise ValueError("В отеле 10 этажей")
        self.floor = floor

        if not isinstance(expensive_room, int):
            raise TypeError("Стоимость дорогого номера должна быть типа int ")
        if expensive_room < 2000:
            raise ValueError("Стоимость дорогого номера минимум 2000")
        self.expensive_room = expensive_room

        if not isinstance(cheap_room, int):
            raise TypeError("Стоимость дешевого номера должна быть типа int ")
        if cheap_room < 1000:
            raise ValueError("Стоимость дорогого номера минимум 1000")
        self.cheap_room = cheap_room

    def financial_opportunity(self) -> str:  # Проверка возможности оплаты номера
        if self.capital >= self.expensive_room or self.capital >= self.cheap_room:
            if self.floor <= 5:
                return 'Клиент сможет позволить себе любой номер на этаже'

            elif self.floor > 5:
                return 'Клиент может позволить себе дешевый номер на этаже'
        else:
            return 'Клиент не может позволить себе номер в отеле'

    def vacation_money_balance(self) -> int: # Нахождение остатка на балансе после оплаты номера
        if self.floor <= 5:
            return self.capital - self.expensive_room

        elif self.floor > 5:
            return self.capital - self.cheap_room

Client_hotel_1 = Client(3000, 7, 5000, 2500)
Client_hotel_2 = Client(4000, 3, 3000, 2500)
Client_hotel_3 = Client(5000, 1, 2000, 1000)

print(Client_hotel_1.financial_opportunity(), Client_hotel_1.vacation_money_balance())
print(Client_hotel_2.financial_opportunity(), Client_hotel_2.vacation_money_balance())


class Beam:
    def __init__(self, height: float, width: float, length: float, reinf: list[list[int, int, float]]):
        """
        Создание и подготовка к работе объекта "Балка"

        :param height: Высота балки
        :param width: Ширина балки
        :param length: Длина балки
        :param reinf: Спецификация Арматуры в балке

        Примеры:
        >>> beam = Beam(400, 400, 5000, [[1, 32, 200], [2, 28, 300]])
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота балки должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота балки должна быть положительным числом")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина балки должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина балки должна быть положительным числом")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("Длина балки должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина балки должна быть положительным числом")
        self.length = length

        if not isinstance(reinf, list):
            raise TypeError("Спецификация арматуры дается списком списков типа list,"
        "с позицией типа int, диаметром арматуры типа int, весом типа int или float")
        self.reinf = reinf

    def is_have_reinforcement(self) -> bool:
        """
        Функция которая проверяет есть ли в балке арматура
        :return: Есть ли арматура в балке

        Примеры:
        >>> beam = Beam(400, 400, 5000, [[1, 32, 200], [2, 28, 300]])
        >>> beam.is_have_reinforcement()
        """
        ...

    def add_rebar(self, diameter: int, weight: float) -> list:
        """
        Функция которая добавляет армирование балке и присваивает позицию

        :param diameter: Диаметр арматуры
        :param weight: Вес арматуры

        :return: Обновленная спецификация армирования

        Примеры:
        >>> beam = Beam(400, 400, 5000, [[1, 32, 200], [2, 28, 300]])
        >>> beam.add_rebar(28, 300)
        """
        if not isinstance(diameter, int):
            raise TypeError("Диаметр арматуры должен быть типа int")
        if diameter <= 0:
            raise ValueError("Диаметр арматуры должен быть положительным числом")

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес арматуры должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес арматуры должен быть положительным числом")
        ...

class Fuel:
        def __init__(self, price: float, distance: float, volume: float, consumption: float):
            """
            Создание и подготовка к работе объекта "Топливо"

            :param price: Стоимость одного литра топлива
            :param distance: Расстояние от А до В
            :param volume: Необходимый объем топлива
            :param consumption: Расход топлива на километр

            Примеры:
            >>> fuel = Fuel(50, 400, 40, 10)
            """
            if not isinstance(price, (int, float)):
                raise TypeError("Стоимость одного литра топлива должна быть типа int или float")
            if price <= 0:
                raise ValueError("Стоимость одного литра топлива должна быть положительным числом")
            self.price = price

            if not isinstance(distance, (int, float)):
                raise TypeError("Расстояние от А до В должно быть типа int или float")
            if distance <= 0:
                raise ValueError("Расстояние от А до В должно быть положительным числом")
            self.distance = distance

            if not isinstance(volume, (int, float)):
                raise TypeError("Необходимый объем топлива должен быть типа int или float")
            if volume <= 0:
                raise ValueError("Необходимый объем топлива должен быть положительным числом")
            self.volume = volume

            if not isinstance(consumption, (int, float)):
                raise TypeError("Расход топлива на километр должен быть типа int или float")
            if consumption <= 0:
                raise ValueError("Расход топлива на километр должен быть положительным числом")
            self.consumption = consumption

        def is_have_fuel(self) -> bool:
            """
            Функция которая проверяет есть ли в баке топливо

            :return: Есть ли топливо в баке

            Примеры:
            >>> fuel = Fuel(50, 400, 40, 10)
            >>> fuel.is_have_fuel()
            """
            ...

        def add_fuel(self, gasoline: float) -> None:
            """
            Функция которая добавляет топливо в бак

            :param gasoline: Количество добавляемого топлива

            :return: Новое количество топлива в баке

            Примеры:
            >>> fuel = Fuel(50, 400, 40, 10)
            >>> fuel.add_fuel(30)
            """

            if not isinstance(gasoline, (int, float)):
                raise TypeError("Объем топлива должен быть типа int или float")
            if gasoline <= 0:
                raise ValueError("Объем топлива должен быть положительным числом")
            ...

if __name__ == "__main__":
        doctest.testmod()
# end
