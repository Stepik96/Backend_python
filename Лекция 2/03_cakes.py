"""Функции, задача 3 (слайд 42): отчёт о фасовке пирожных."""


def print_pack_report(cake_count):
    """Перебрать количества от cake_count до 1 и вывести отчёт."""
    for count in range(cake_count, 0, -1):
        if count % 3 == 0 and count % 5 == 0:
            print(count, "- расфасуем по 3 или по 5")
        elif count % 5 == 0:
            print(count, "- расфасуем по 5")
        elif count % 3 == 0:
            print(count, "- расфасуем по 3")
        else:
            print(count, "- не заказываем!")


if __name__ == "__main__":
    cake_count = int(input("Количество пирожных (больше 1): "))
    print_pack_report(cake_count)
