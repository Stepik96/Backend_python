"""Функции, задача 4 (слайд 43): настраиваемый генератор паролей."""

import random
import secrets
import string


def ask_setting(question):
    """Прочитать настройку: д — да, любой другой ответ — нет."""
    return input(question + " (д/н): ").strip().lower() == "д"


def generate_password(length, symbol_groups):
    """Добавить по символу из каждой группы и заполнить остаток."""
    password_symbols = []
    for group in symbol_groups:
        password_symbols.append(secrets.choice(group))
    all_symbols = "".join(symbol_groups)
    for _ in range(length - len(symbol_groups)):
        password_symbols.append(secrets.choice(all_symbols))
    random.SystemRandom().shuffle(password_symbols)
    return "".join(password_symbols)


if __name__ == "__main__":
    print("=== Генератор паролей ===")
    length = int(input("Длина пароля: "))
    symbol_groups = []
    if ask_setting("Добавить строчные буквы"):
        symbol_groups.append(string.ascii_lowercase)
    if ask_setting("Добавить заглавные буквы"):
        symbol_groups.append(string.ascii_uppercase)
    if ask_setting("Добавить цифры"):
        symbol_groups.append(string.digits)
    if ask_setting("Добавить спецсимволы"):
        symbol_groups.append("!@#$%^&*")
    if not symbol_groups:
        print("Нужно выбрать хотя бы одну группу символов.")
    elif length < len(symbol_groups):
        print("Длина должна быть не меньше числа выбранных групп.")
    else:
        print("Ваш пароль:", generate_password(length, symbol_groups))
