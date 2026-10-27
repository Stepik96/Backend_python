"""Задачи 1–4 (слайды 11, 19, 27, 31): книги и основы ООП."""

from abc import ABC, abstractmethod
from datetime import date


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        """Вывести информацию об объекте."""


class Book(Printable):
    def __init__(self, title, author, year):
        if not title.strip() or not author.strip():
            raise ValueError("Название и автор не должны быть пустыми.")
        if type(year) is not int or not 1 <= year <= date.today().year:
            raise ValueError("Год должен быть между 1 и текущим годом.")
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"{self.title} — {self.author}, {self.year} г."

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return (self.title, self.author, self.year) == (
            other.title,
            other.author,
            other.year,
        )

    @property
    def age(self):
        """Возраст в годах относительно текущего года."""
        return date.today().year - self.year

    @age.setter
    def age(self, value):
        if type(value) is not int or not 0 <= value < date.today().year:
            raise ValueError("Недопустимый возраст книги.")
        self.year = date.today().year - value

    @classmethod
    def from_string(cls, text):
        """Создать книгу из строки «Название;Автор;Год»."""
        parts = [part.strip() for part in text.split(";")]
        if len(parts) != 3:
            raise ValueError("Ожидается строка Название;Автор;Год.")
        return cls(parts[0], parts[1], int(parts[2]))

    def print_info(self):
        print(self.info())


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        if not format.strip():
            raise ValueError("Укажите формат электронной книги.")
        self.format = format.upper()

    def info(self):
        return f"{super().info()} Формат: {self.format}."

    def __eq__(self, other):
        result = super().__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return result and self.format == other.format

    @classmethod
    def from_string(cls, text):
        """Создать электронную книгу: «Название;Автор;Год;Формат»."""
        parts = [part.strip() for part in text.split(";")]
        if len(parts) != 4:
            raise ValueError("Ожидается строка Название;Автор;Год;Формат.")
        return cls(parts[0], parts[1], int(parts[2]), parts[3])


if __name__ == "__main__":
    book = Book("Капитанская дочка", "А. С. Пушкин", 1836)
    copy = Book.from_string("Капитанская дочка;А. С. Пушкин;1836")
    ebook = Ebook.from_string("Мастер и Маргарита;М. А. Булгаков;1967;epub")
    book.print_info()
    print("Книги равны:", book == copy)
    print("Возраст книги:", book.age)
    copy.age = 10
    print("После изменения возраста:", copy)
    ebook.print_info()
