#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

number = int(input("Введите число: "))
catalog = [10, 20, 30, 40,50]
cnt = catalog.count(number)
for value in catalog:
    if cnt > 0:
        index_number = catalog.index(number)
        catalog.insert(index_number+cnt, number)
        break
    else:
        if number > value:
            index_value = catalog.index(value)
            catalog.insert(index_value, number)
            break
        elif number < catalog[len(catalog) - 1]:
            catalog.append(number)
print(catalog)