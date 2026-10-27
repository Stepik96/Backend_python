"""Задачи 3–4 (слайды 33–34): сложение и исправленное деление."""


def add_numbers(first_number: float, second_number: float) -> float:
    """Вернуть сумму двух чисел."""
    return first_number + second_number


def divide(first_number: float, second_number: float):
    """Вернуть частное или None, если делитель равен нулю."""
    if second_number == 0:
        return None
    return first_number / second_number


if __name__ == "__main__":
    first_number = float(input("Первое число: "))
    second_number = float(input("Второе число: "))
    print("Сумма:", add_numbers(first_number, second_number))
    quotient = divide(first_number, second_number)
    if quotient is None:
        print("На ноль делить нельзя")
    else:
        print("Частное:", quotient)
