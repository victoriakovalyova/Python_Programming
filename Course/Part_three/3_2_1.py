#Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: keykey и valuevalue.

#Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
#Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 ∗ key. Если и ключа 2 ∗ key нет, 
#то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

#Требуется реализовать только эту функцию, кода вне её не должно быть.
#Функция не должна вызывать внутри себя функции input и print.
def update_dictionary(d, key, value):
    d = {}
    if key in d == True:
        d[key] = [value]
    elif key not in d == True:
        d[2 * key] = [value]
    elif 2 * key not in d == True:
        d[2 * key] = [value]