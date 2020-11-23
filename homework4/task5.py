#Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce


def f_list_formation(param1, param2):
    return param1 * param2

print(f'Список четных значений {[param2 for param2 in range(99, 1001) if param2 % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(f_list_formation, [param2 for param2 in range(99, 1001) if param2 % 2 == 0])}')