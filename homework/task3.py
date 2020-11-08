#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input("Укажите число: "))
first_calc = number + number
second_calc = first_calc + number
last_calc = second_calc + number
print(f"Первое вычисление: {first_calc}\nВторое вычисление: {second_calc}\nИтог: {last_calc}")