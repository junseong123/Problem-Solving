N, M, K = map(int, input().split())
arr = []
sum = 0
for i in range(N):
    line = []
    for j in range(M):
        if sum == K:
            print(i, j)
            exit()
        else:
            line.append(sum)
            sum += 1
    arr.append(line)
