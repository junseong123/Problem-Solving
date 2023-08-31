N = int(input())
a = []
b = []
cnt = 0
if N >= 1:
    for i in range(N):
        a.append(list(map(int, input().split())))
else:
    print(-1)  # N이 0이하일 경우 -1 출력


for i in range(N):
    if a[i][0] <= a[i][1]:
        b.append(a[i][1])
        cnt += 1
if cnt == 0:
    print(-1)
else:
    b.sort()
    print(b[0])
