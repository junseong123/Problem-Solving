N, K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
for i in range(N):
    if K >= coin[i]:
        print(coin[i])
        K -= coin[i]
    elif K == 0:
        break
    elif K < coin[i]:
        continue
