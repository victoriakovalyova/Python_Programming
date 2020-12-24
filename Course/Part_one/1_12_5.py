a = int(input())
b = int(input())
c = int(input())
if b <= a >= c:
    print(a)
    if a >= b <= c:
        print(b)
        print(c)
    elif a >= c <= b:
        print(c)
        print(b)
elif a <= b >= c:
    print(b)
    if b >= a <= c:
        print(a)
        print(c)
    elif a >= c <= b:
        print(c)
        print(a)
elif a <= c >= b:
    print(c)
    if b >= a <= c:
        print(a)
        print(b)
    elif a >= b <= c:
        print(b)
        print(a)
