x = int(input())
check = 0
for i in range(2, x // 2 + 1):
    if x % i == 0:
        check = check + 1
print(check <= 0)
