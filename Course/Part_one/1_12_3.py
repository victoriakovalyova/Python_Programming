
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