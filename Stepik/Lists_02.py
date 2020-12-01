a = [int(i) for i in input().split()]
result = []
if len(a) == 1:
    result.append(a)
else:
    for n in a[:-1]:
        left = a.index(n) - 1
        right = a.index(n) + 1
        result.append(a[left] + a[right])
    result.append(a[-2] + a[0])
print(result)