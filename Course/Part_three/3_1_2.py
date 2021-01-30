#Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
#удаляет из него все нечётные значения, а чётные нацело делит на два.
#Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
def modify_list(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(int(i / 2))
    lst.clear()
    lst.extend(result)
array = [1, 55, 3, 2, 88, 10000]
modify_list(array)
print(array)
#def modify_list(l):
#    for x in l[:]: #решение через копию массива [:]
#        if x % 2 == 0:
#            l.append(x//2)
#        l.remove(x)
#array = [1, 55, 3, 2, 88, 10000]
#modify_list(array)
#print(array)