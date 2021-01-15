#Напишите программу, на вход которой подается одна строка с целыми числами. 
#Программа должна вывести сумму этих чисел.

#Используйте метод split строки. 
string = input()
array = string.split()
counter = 0 
for i in array:
    counter += int(i)
print(counter)