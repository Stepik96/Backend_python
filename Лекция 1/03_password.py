# Задача 3 (слайд 18): 3 заглавные буквы, 3 цифры, 2 спецсимвола.
import random
import string

password_symbols = []
for _ in range(3):
    password_symbols.append(random.choice(string.ascii_uppercase))
for _ in range(3):
    password_symbols.append(random.choice(string.digits))
for _ in range(2):
    password_symbols.append(random.choice("!@#$%^&*"))
random.shuffle(password_symbols)
print("Пароль:", "".join(password_symbols))
