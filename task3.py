# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

from random import randint


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT) 
counter = 0
flag = False
while counter <= 10:
    user_number = int(input("Введите число: "))
    counter += 1
    if user_number == num:
        print(f"Вы угадали с попытки номер {counter}!!!")
        flag = True
        break
    
    if user_number < num:
        print(f"Попытка {counter}: больше")
    else:
        print(f"Попытка {counter}: меньше")

if flag:
    print("Вы выиграли!")
else:
    print("Вы проиграли")