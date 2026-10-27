"""Задача 5: поиск простых чисел решетом Эратосфена."""


def prime_numbers(limit):
    """Вернуть простые числа до limit включительно; ниже 2 список пуст."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    number = 2
    while number * number <= limit:
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
        number += 1
    return [number for number in range(2, limit + 1) if is_prime[number]]


if __name__ == "__main__":
    try:
        limit = int(input("Введите целое N: "))
    except ValueError:
        print("Ошибка: введите целое число.")
    else:
        print("Простые числа:", *prime_numbers(limit))
