n = str(input())
if n == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c) / 2)
    S = (float((p * (p - a) * (p - b) * (p - c))** 0.5))
    print(S)
elif n == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
elif n == 'круг':
    r = int(input())
    Pi = 3.14
    print(float(Pi * (r ** 2)))