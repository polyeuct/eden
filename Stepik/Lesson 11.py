mtx = [[int(i) for i in input().split()]]
X = input()
while X != 'end':
    mtx.append([int(i) for i in X.split()])
    X = input()
if len(mtx) == 1:
    print(mtx[0][0] * 4)
else:
    for row in range(len(mtx)):
        for col in range(len(mtx[row])):
            if row == len(mtx) - 1:
                row = -1
            if col == len(mtx[row]) - 1:
                col = -1
            print((mtx[row - 1][col] + mtx[row + 1][col]) + (mtx[row][col - 1] + mtx[row][col + 1]), end=' ')
        print()
