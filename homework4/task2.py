#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

array = [10, 20, 31, 40, 50, 60]
result = [element for num, element in enumerate(array) if array[num - 1] < array[num]]
print(f'Начальный массив {array}')
print(f'Конечный массив {result}')