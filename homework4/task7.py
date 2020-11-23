#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

from itertools import count
from math import factorial

def factorial_create():
    for i in count(1):
        yield factorial(i)

result = factorial_create()
x = 0
for i in result:
    if x < 15:
        print(i)
        x += 1
    else:
        break