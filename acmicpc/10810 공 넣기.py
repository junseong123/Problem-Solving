n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    a.append(list(map(int, input().split())))
    for k in range(a[i][0], a[i][1] + 1):
        if a[i][1] > n:
            continue
        b.append(a[i][2])
print(b)
