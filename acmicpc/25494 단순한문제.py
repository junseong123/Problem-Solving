t = int(input())
a = []
b = []

for i in range(t):
    cnt = 0
    a.append(list(map(int, input().split())))
    for x in range(1, a[i][0] + 1):
        for y in range(1, a[i][1] + 1):
            for z in range(1, a[i][2] + 1):
                if x % y == y % z and z % x == y % z:
                    cnt += 1
    print(cnt)
