"""Функции, задача 1 (слайд 40): шифр Цезаря."""

ENGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def detect_language(text):
    """Определить язык по буквам текста."""
    has_russian = False
    has_english = False
    for symbol in text.lower():
        if symbol in RUSSIAN_ALPHABET:
            has_russian = True
        elif symbol in ENGLISH_ALPHABET:
            has_english = True
    if has_russian and has_english:
        return "русский и английский"
    if has_russian:
        return "русский"
    if has_english:
        return "английский"
    return "букв нет"


def caesar_cipher(text, shift):
    """Сдвинуть буквы, сохраняя регистр, пробелы и знаки препинания."""
    result = ""
    for symbol in text:
        lower_symbol = symbol.lower()
        if lower_symbol in RUSSIAN_ALPHABET:
            alphabet = RUSSIAN_ALPHABET
        elif lower_symbol in ENGLISH_ALPHABET:
            alphabet = ENGLISH_ALPHABET
        else:
            result += symbol
            continue
        new_index = (alphabet.index(lower_symbol) + shift) % len(alphabet)
        new_symbol = alphabet[new_index]
        if symbol.isupper():
            new_symbol = new_symbol.upper()
        result += new_symbol
    return result


if __name__ == "__main__":
    text = input("Введите текст: ")
    shift = int(input("Сдвиг: "))
    action = input("1 — шифровать, 2 — дешифровать: ")
    print("Язык:", detect_language(text))
    if action == "2":
        shift = -shift
    print(caesar_cipher(text, shift))
