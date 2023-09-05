a = []
b = []
count = 0
for i in range(7):
    a.append(int(input()))
    if a[i] % 2 != 0:
        count += 1
        b.append(a[i])

if count == 0:
    print(-1)
else:
    print(sum(b))
    print(min(b))
