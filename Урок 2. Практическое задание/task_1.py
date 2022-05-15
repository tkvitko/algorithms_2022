"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


# def calc_cycle():
#     while True:
#         operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
#         if operator == '0':
#             break
#         try:
#             a = int(input('Введите первое число:  '))
#             b = int(input('Введите второе число:  '))
#             result = eval(f'{a}{operator}{b}')
#             print(f'Ваш результат {result}')
#         except ZeroDivisionError:
#             print('На 0 делить нельзя')
#         except ValueError:
#             print('Вы ввели не число')


def calc_recursion():
    operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operator == '0':
        return

    try:
        a = int(input('Введите первое число:  '))
        b = int(input('Введите второе число:  '))
        result = eval(f'{a}{operator}{b}')
        print(f'Ваш результат {result}')
    except ZeroDivisionError:
        print('На 0 делить нельзя')
    except ValueError:
        print('Вы ввели не число')

    if operator == '0':
        return
    else:
        calc_recursion()


if __name__ == '__main__':
    # calc_cycle()
    calc_recursion()
