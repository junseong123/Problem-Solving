k = int(input())
D1, D2 = map(int, input().split())
if k**2 - ((D1 - D2) / 2) ** 2 == k**2 - ((D1 - D2) // 2) ** 2:
    print(k**2 - ((D1 - D2) // 2) ** 2)
else:
    print(k**2 - ((D1 - D2) / 2) ** 2)
