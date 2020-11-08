#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

current_result = float(input("Укажите текущий результат: "))
need_result = float(input("Укажите желаймый результат: "))
result_day = 1

if current_result > need_result:
    print(result_day)
while current_result < need_result:
    current_result = current_result + current_result/10
    result_day += 1
    print(f"Результат на день {result_day}: {round(current_result,2)}")

print(f"\n>>Желаймый результат будет достигнут в {result_day} день.<<")