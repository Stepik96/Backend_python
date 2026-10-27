"""Функции, задача 5 (слайд 44): конвертер римских чисел."""


def to_roman(number):
    """Перевести целое число от 1 до 3999 в римскую запись."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Нужно целое число от 1 до 3999.")
    if not 1 <= number <= 3999:
        raise ValueError("Число должно быть от 1 до 3999.")
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]
    result = ""
    for value, symbol in zip(values, symbols):
        while number >= value:
            result += symbol
            number -= value
    return result


def from_roman(roman_number):
    """Перевести корректное римское число в обычное."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_number = roman_number.strip().upper()
    if not roman_number or any(c not in values for c in roman_number):
        raise ValueError("Некорректное римское число.")
    result = 0
    for index, symbol in enumerate(roman_number):
        value = values[symbol]
        if (
            index + 1 < len(roman_number)
            and value < values[roman_number[index + 1]]
        ):
            result -= value
        else:
            result += value
    if not 1 <= result <= 3999 or to_roman(result) != roman_number:
        raise ValueError("Некорректное римское число.")
    return result


if __name__ == "__main__":
    print("1 — обычное число в римское")
    print("2 — римское число в обычное")
    action = input("Выберите действие: ").strip()
    try:
        if action == "1":
            print(to_roman(int(input("Введите число от 1 до 3999: "))))
        elif action == "2":
            print(from_roman(input("Введите римское число: ")))
        else:
            print("Выберите 1 или 2.")
    except ValueError as error:
        print("Ошибка:", error)
