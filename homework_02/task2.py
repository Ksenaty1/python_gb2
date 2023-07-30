# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def nod(num1, num2):
    while num1 != 0 and num2 != 0:
        
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
            
    return num1 + num2 

def nok(num1, num2):
    return int((num1 * num2) / nod(num1, num2))


numerator1, denominator1 = map(int, input('Введите первую дробь вида a/b: ').split('/'))
numerator2, denominator2 = map(int, input('Введите вторую дробь вида a/b: ').split('/'))


# Находим сумму 
sum_denominator = nok(denominator1, denominator2)
sum_numerator = int(numerator1 * (sum_denominator / denominator1) + numerator2 * (sum_denominator / denominator2))
print('Сумма: ' + str(sum_numerator) + '/' + str(sum_denominator))

# Находим произведение
multiply_numerator = numerator1 * numerator2
multiply_denominator = denominator1 * denominator2
print('Произведение: ' + str(multiply_numerator) + '/' + str(multiply_denominator))

# Проверяем с помощью модуля Fraction
print('Ответ с помощью модуля fractions')
print('Сумма: ', Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2))
print('Произведение: ', Fraction(numerator1, denominator1) * Fraction(numerator2, denominator2))
