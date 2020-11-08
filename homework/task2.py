#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Укажите время в секундах: "))
hour = time // 3600
current_time = time % 3600
minute = current_time // 60
second = current_time % 60
print(f"{hour}:{minute}:{second}")