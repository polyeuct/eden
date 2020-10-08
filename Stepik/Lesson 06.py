n = int(input())
x10 = n % 10
x100 = n % 100
if n < 0 or n > 1000:
    print('Вы ввели неверное значение!')
elif x10 == 1 and x100 != 11:
    print(n, 'программист')
elif (x10 == 2 or x10 == 3 or x10 == 4) and (x100 != 12 or x100 != 13 or x100 != 14):
    print(n, 'программиста')
else:
    print(n, 'программистов')
