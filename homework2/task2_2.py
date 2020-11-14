#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

catalog = ['g', 'e', 'e', 'k', 'b', 'r', 'a', 'i', 'n', 's']
if len(catalog) % 2 == 0:
    i = 0
    while i < len(catalog):
        values = catalog[i]
        catalog[i] = catalog[i+1]
        catalog[i+1] = values
        i += 2
else:
    i = 0
    while i < len(catalog) - 1:
        values = catalog[i]
        catalog[i] = catalog[i + 1]
        catalog[i + 1] = values
        i += 2
print(catalog)