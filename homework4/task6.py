 #Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count

for i in count(int(input('Укажите число число '))):
    print(i)

from itertools import cycle

array = [True, 'geekbr', 42]
for i in cycle(array):
    print(i)