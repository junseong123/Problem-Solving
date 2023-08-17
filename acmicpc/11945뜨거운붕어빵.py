n, m = map(int, input().split())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
for i in range(n):
    print(*reversed(x[i]))
