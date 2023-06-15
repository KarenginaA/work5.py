# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# number_a = int(input("Введите число "))
# number_b = int(input("Введите степень числа(целое неотрицательно число) "))

# def func(number_a, number_b):
#     if number_b == 0:
#         return 1

#     return func(number_a, number_b - 1) * number_a


# print(func(number_a, number_b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 
# digit_a = int(input("Введите первое неотрицительное число "))
# digit_b = int(input("Введите второе неотрицательно число "))


# def recursive_sum(digit_a, digit_b):
#     if digit_a == 0:
#         return digit_b
#     else:
#         return recursive_sum(digit_a - 1, digit_b + 1)


# print(recursive_sum(digit_a, digit_b))