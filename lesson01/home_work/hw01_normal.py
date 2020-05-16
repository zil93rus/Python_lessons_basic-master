
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

x = 583759
xMax = 0
while x != 0:
    y = x % 10
    x //= 10
    if y > xMax:
        xMax = y
print(f"This is cycle while - {xMax}")

x = 34736
xMax = 0
for i in str(x):
    if int(i) > xMax:
        xMax = int(i)
print(f"This is cycle for - {xMax}")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = input("Enter number a: ")
b = input("Enter number b: ")
print(f"You enter: a - {a}, b - {b}")
a, b = (b, a)
print(f"Decision with two variable: a - {a}, b - {b}")

a = input("Enter number a: ")
b = input("Enter number b: ")
print(f"You enter: a - {a}, b - {b}")
a, b = b, a
print(f"Tuple decision: a - {a}, b - {b}")




# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
print("ax² + bx + c = 0")
a = int(input("Enter number a - "))
b = int(input("Enter number b - "))
c = int(input("Enter number c - "))

D = b * b - 4 * a * c
if D < 0:
    print("No roots, Good bye!")
if D == 0:
    print("One root")
    x = -b + math.sqrt(D) / 2 * a
    print(f"x - {x}")
if D > 0:
    print("Two roots")
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"x1 - {int(x1)}, x2 - {int(x2)}")

