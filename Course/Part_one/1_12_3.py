#Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число,
#второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

#Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

#Обратите внимание, что на вход программе приходят вещественные числа.
a = (float(input()))
b = (float(input()))
d = (str(input())) #mod
if d == 'pow':
    print(a ** b)
elif d == '*':
    print(a * b)
elif d == '+':
    print(a + b)
elif d == '-':
    print(a - b)
elif d == 'mod':
    print(a % b)
elif (d == 'mod' or d == '/' or d == 'div') and (b == 0):
     print('Деление на 0!')
elif d == '/':
    print(a / b)
elif d == 'div':
    print(a // b)