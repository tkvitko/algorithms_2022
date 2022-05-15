"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_recursion(count, summ=1, current=1):
    if count == 0:
        return summ
    else:
        count -= 1
        current /= -2
        summ += current
        return sum_recursion(count, summ, current)


if __name__ == '__main__':
    count = int(input('Введите количество шагов: '))
    print(sum_recursion(count - 1))
