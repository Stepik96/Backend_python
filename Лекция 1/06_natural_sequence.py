# Задача 6 (слайд 31): позиции считаются с 1.
position = int(input("Введите позицию N: "))
digit_count = 1
first_number = 1
numbers_in_block = 9
# Пропускаем блоки: 1..9, 10..99, 100..999 и так далее.
while position > digit_count * numbers_in_block:
    position -= digit_count * numbers_in_block
    digit_count += 1
    first_number *= 10
    numbers_in_block *= 10
number = first_number + (position - 1) // digit_count
digit_index = (position - 1) % digit_count
print(str(number)[digit_index])
