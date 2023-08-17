N, M, K = map(int, input().split())
arr = []
s = 0
for i in range(N):
    line = []
    for j in range(M):
        if s == K:
            print(i, j)
            exit()
        else:
            line.append(s)
            s += 1
    arr.append(line)
