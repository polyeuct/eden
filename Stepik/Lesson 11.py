row = [[int(i) for i in input().split()]]
X = input()
while X != 'end':
    row.append([int(i) for i in X.split()])
    X = input()
for i in range(len(row)):
    for j in range(len(row[i])):
        if i == len(row) - 1:
            i = -1
        if j == len(row[i]) - 1:
            j = -1
        print((row[i - 1][j] + row[i + 1][j]) + (row[i][j - 1] + row[i][j + 1]), end=' ')
    print()
