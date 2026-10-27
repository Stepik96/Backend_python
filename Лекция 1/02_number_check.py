# Задача 2 (слайд 14): проверка целого числа.
number = int(input("Введите целое число: "))
if number % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
if number > 0:
    print("Положительное")
elif number < 0:
    print("Отрицательное")
else:
    print("Ноль")
if 10 <= number <= 50:
    print("Принадлежит диапазону [10, 50]")
else:
    print("Не принадлежит диапазону [10, 50]")
