n = int(input())
a = 1
for i in range(1, n + 1):
    a *= i
s = a // 7 // 24 // 60 // 60
print(s)
