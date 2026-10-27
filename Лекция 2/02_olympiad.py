"""Функции, задача 2 (слайд 41): попадание в тройку лидеров."""


def check_winners(scores, student_score):
    """Напечатать, входит ли результат студента в три лучших."""
    top_scores = sorted(scores, reverse=True)[:3]
    if student_score in top_scores:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


if __name__ == "__main__":
    scores = list(map(int, input("Баллы участников через пробел: ").split()))
    student_score = int(input("Баллы Стаса: "))
    check_winners(scores, student_score)
