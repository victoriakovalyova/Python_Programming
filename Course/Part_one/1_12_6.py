n = int(input())
if n % 10 == 1 and n % 100 != 11:
    print( n, 'программист')
elif n % 10 == 2 and n % 100 != 12:
    print( n, 'программиста')
elif n % 10 == 3 and n % 100 != 13:
    print( n, 'программиста')
elif n % 10 == 4 and n % 100 != 14:
    print( n, 'программиста')
else:
    print( n, 'программистов')