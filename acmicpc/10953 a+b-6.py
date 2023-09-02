T = int(input())
a = []
for i in range(T):
    a.append(list(map(int, input().split(","))))
    print(a[i][0] + a[i][1])
