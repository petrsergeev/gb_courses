# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = abs(int(input("Укажите положительное число: ")))
max_number = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра в указанном числе ", max_number)
        break
