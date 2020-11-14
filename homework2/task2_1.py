# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


catalog = [True, 42, -485, 3.14, "Test"]
def catalog_types(values):
    for values in range(len(catalog)):
        print(type(catalog[values]))
    return
catalog_types(catalog)