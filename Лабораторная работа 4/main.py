class Trucks:
    """
    Базовый класс Грузовые автомобили
    """
    def __init__(self, car_brand: str, size: str, speed: int, cargo: int, power_reserve: int):
        """
        :param car_brand: Марка авто
        :param size: Размер авто, габариты м.
        :param speed: Максимальная скорость, км.ч
        :param cargo: Вместимость груза, т.
        :param power_reserve: Запас хода, км.
        Пример
        >>> trucks = Trucks ("Liebherr", "12700х5595х3710", 80, 450, 100)
        """
        self._car_brand = car_brand  # Защищенный атрибут
        self._size = size
        self._speed = speed
        self._cargo = cargo
        self._power_reserve = power_reserve

        if not isinstance(speed, int):
            raise TypeError('Максимальная скорость должна быть типа int')
        if speed <= 0:
            raise ValueError('Максимальная скорость должна быть положительным числом')
        self.speed = speed

        if not isinstance(cargo, int):
            raise TypeError('Вместимость груза должна быть типа int')
        if cargo <= 0:
            raise ValueError('Вместимость груза должна быть положительным числом')
        self.cargo = cargo

        if not isinstance(power_reserve, int):
            raise TypeError('Запас хода должен быть типа int')
        if power_reserve <= 0:
            raise ValueError('Запас хода должен быть положительным числом')
        self.power_reserve = power_reserve

    @property  # защищаем атрибут от изменений
    def car_brand(self) -> str:
        """Функция возвращает марку авто"""
        return self._car_brand

    def __str__(self):
        return f"Марка авто: {self._car_brand}, Размер: {self._size}, Максимальная скорость: {self._speed}, " \
               f"Вместимость груза: {self._cargo}, Запас хода: {self._power_reserve}"

    def __repr__(self):
        return f"{self.__class__.__name__}(car_brand={self._car_brand!r}, size={self._size!r}, speed={self._speed!r}),"\
               f"cargo={self._cargo!r}, power_reserve={self._power_reserve!r})"

    def cargo_turnover(self) -> int:
        """
        Грузооборот — показатель отражения объёма перевозок в грузо-километрах и исчисляется как произведение
        количества груза на расстояние перевозок.
        return self.cargo * (self.power_reserve / self.speed)
         """

class Mining_truck(Trucks):
    """
    Дочерний класс - Карьерный самосвал
    """
    def __init__(self, car_brand: str, size: str, speed: int, cargo: int, power_reserve: int, max_quarry_slope: int):
        """
        Создание и подготовка к работе обьекта класса "Карьерный самосвал"
        :param car_brand: Марка авто
        :param size: Размер авто, габариты м.
        :param speed: Максимальная скорость, км.ч
        :param cargo: Вместимость груза, т.
        :param power_reserve: Запас хода, км.
        :param max_quarry_slope: Максимальный уклон карьера, градус
        Пример
        >>> mining_truck = Mining_truck ("Liebherr", "12700х5595х3710", 80, 450, 100, 36)
        """
        super().__init__(car_brand, size, speed, cargo, power_reserve)
        self.max_quarry_slope = max_quarry_slope

        if not isinstance(max_quarry_slope, int):
            raise TypeError('Максимальный уклон карьера должен быть типа int')
        if max_quarry_slope <= 0:
            raise ValueError('Максимальный уклон карьера должен быть положительным числом')
        self._max_quarry_slope = max_quarry_slope

    def __str__(self):
        return f"Марка авто: {self._car_brand}, Размер: {self._size}, Максимальная скорость: {self._speed}, " \
               f"Вместимость груза: {self._cargo}, Запас хода: {self._power_reserve}, Уклон: {self._max_quarry_slope}"

    def __repr__(self):
        return f"{self.__class__.__name__}(car_brand={self._car_brand!r}, size={self._size!r}, speed={self._speed!r}),"\
               f"cargo={self._cargo!r}, power_reserve={self._power_reserve!r}, max_quarry_slope={self._max_quarry_slope!r})"

    def power_reserve_reduction(self) -> int:
        """
        Уклон карьера влияет на увеличение расхода топлива, а следовательно на снижение запаса хода,
        Определим запас хода под уклоном, где 36 - уклон карьера, 180 - горизонтальная плоскость

        return self.power_reserve * (1 - 36 / 180)
        """


if __name__ == "__main__":
    pass
#end