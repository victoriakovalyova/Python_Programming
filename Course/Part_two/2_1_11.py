#Напишите программу, которая считывает со стандартного ввода целые числа,
#по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
total = 0
condition = 5
while condition != 0:
    condition = int(input())
    total += condition
    if condition == 0:
        print(total)