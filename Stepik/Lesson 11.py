lst = [[int(i) for i in input().split()]]
X = input()
while X != 'end':
    lst.append([int(i) for i in X.split()])
    X = input()
print(lst)
