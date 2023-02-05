class Book:
    """ Базовый класс книги. """
    def __init__(self, _name: str, _author: str):
        self._name = _name
        self._author = _author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, _name: str, _author: str, _pages: int):
        super().__init__(_name, _author)
        self._pages = _pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, _pages: int):
        if not isinstance(_pages, int):
            raise TypeError("Тип данных должен быть int")
        if _pages <= 0:
            raise ValueError("Число должно быть положительным")
        self._pages = _pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, _name: str, _author: str, _duration: float):
        super().__init__(_name, _author)
        self._duration = _duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, _duration: float):
        if not isinstance(_duration, float):
            raise TypeError("Тип данных должен быть float")
        if _duration <= 0:
            raise ValueError("Число должно быть положительным")
        self._duration = _duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"
#end