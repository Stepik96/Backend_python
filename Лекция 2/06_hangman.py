"""Функции, задача 6 (слайд 45): игра «Виселица»."""

import random


def show_word(word, guessed_letters):
    """Показать угаданные буквы; остальные заменить подчёркиваниями."""
    visible_letters = []
    for letter in word:
        if letter in guessed_letters:
            visible_letters.append(letter)
        else:
            visible_letters.append("_")
    print(" ".join(visible_letters))


def play_hangman():
    """Дать игроку шесть ошибочных попыток на угадывание слова."""
    word = random.choice(
        ["питон", "книга", "компьютер", "программа", "студент"]
    )
    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6
    stages = [
        "",
        "Голова",
        "Голова, тело",
        "Голова, тело, одна рука",
        "Голова, тело, две руки",
        "Голова, тело, две руки, одна нога",
        "Голова, тело, две руки, две ноги",
    ]
    print("=== Виселица ===")
    while mistakes < max_mistakes:
        show_word(word, guessed_letters)
        print("Осталось ошибок:", max_mistakes - mistakes)
        letter = input("Введите одну русскую букву: ").strip().lower()
        if (
            len(letter) != 1
            or letter not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        ):
            print("Введите ровно одну русскую букву.")
            continue
        if letter in guessed_letters:
            print("Эту букву уже называли.")
            continue
        guessed_letters.add(letter)
        if letter not in word:
            mistakes += 1
            print(stages[mistakes])
        if all(letter in guessed_letters for letter in word):
            print("Победа! Слово:", word)
            return
    print("Вы проиграли. Слово:", word)


if __name__ == "__main__":
    play_hangman()
