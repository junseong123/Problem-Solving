a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    profit = c - b
    print(a // profit + 1)
