x = int(input())
y = int(input())
if y == 0:
    print('Please, try again')
    y = int(input())
    if y == 0:
        print('Please, try again')
        y = int(input())
        if y == 0:
            print('Error: division by zero')
if y != 0:
    print(x / y)
