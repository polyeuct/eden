a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
print(float((p * (p - a) * (p - b) * (p - c)) ** 0.5))
