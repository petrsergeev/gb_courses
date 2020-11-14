#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Укажите число: "))
if number <= 12 and number >= 1:
    calendar_dict = \
        {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель",
            5: "Май",
            6: "Июнь",
            7: "Июль",
            8: "Август",
            9: "Сентябрь",
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь"
        }
    calendar_list = list(calendar_dict.values())
    for i, el in enumerate(calendar_list):
        if i == number-1:
            print(f"Месяц с использованием list: {calendar_list[i]}")
            break
    print(f"Месяц с использованием dict: {calendar_dict[number]}")
