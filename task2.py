# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def is_prime(num):
    k = 0
    for i in range(2, num // 2+1):
        if num % i == 0:
            return False
    return True


while True:
    number = int(input("Введите число: "))
    if number > 0 and number < 100.000:
        break
    print("Введите число больше нуля и меньше 100.000")
    
if is_prime(number):
    print("Простое число")
else:
    print("Составное число")