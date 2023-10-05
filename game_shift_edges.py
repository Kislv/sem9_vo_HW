"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

MIN_NUMBER = 1
MAX_NUMBER = 100
ITERATIONS_NUMBER = 1000


def game_core_v3(number: int = 1) -> int:
    """Изначально случайное число генерируем из диапазона
    максимального и минимального значения,
    которое может принять число, которое требуется угадать.
    Затем сравниваем предсказанное число с искомым,
    если значение искомого больше,
    то на следующей итерации предсказываем значение
    случайного числа из диапазона от предыдущего значения предсказанного числа
    до предыдущего максимального значения,
    если значение искомого меньше,
    то на следующей итерации предсказываем значение
    случайного числа из диапазона от предыдущего минимального значения
    до предыдущего значения предсказанного числа

    Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    left = MIN_NUMBER
    right = MAX_NUMBER

    while True:
        count += 1
        predict_number = np.random.randint(left,
                                           right + 1)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        # edge = int((left + right) / 2)
        edge = (predict_number)
        if number > predict_number:
            left = edge
        else:
            right = edge
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов
    угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        MIN_NUMBER,
        MAX_NUMBER + 1,
        size=(ITERATIONS_NUMBER))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
