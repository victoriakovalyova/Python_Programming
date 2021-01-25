#Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
#которые встречаются в нём более одного раза.

#Для решения задачи может пригодиться метод sort списка.

#Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
string = input()
array = [int(x) for x in string.split()] #[1,2. 2.3.7.7.8]
array = array.sort()
print(array)
counter = 0
current = "" 
result = ""
for i in array:
    if current == i:
        counter += 1 
    else:
        if counter > 1:
            result += i + " "
        current = i
        counter = 1
print(result)

