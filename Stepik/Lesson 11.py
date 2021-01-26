row = [[int(i) for i in input().split()]]
X = input()
col = []
while X != 'end':
    row.append([int(i) for i in X.split()])
    X = input()
for j in range(len(row)):
    for i in range(len(row)):
        col += [row[i][j]]
print(row)
print(col)

