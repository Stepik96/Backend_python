# Задача 1 (слайд 5): перевод температуры.
celsius = float(input("Температура в градусах Цельсия: "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f"{celsius:g}°C = {fahrenheit:.2f}°F")
print(f"{celsius:g}°C = {kelvin:.2f}K")
