n = int(input())
x = 0
tmp = 0
while x <= 30:
    if n == 2**x:
        tmp = 1
        break
    else:
        tmp = 0
    x += 1
print(tmp)
