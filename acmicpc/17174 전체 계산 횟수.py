N, M = map(int, input().split())
sum = N
while True:
    N = N // M
    sum += N
    if N < M:
        break
print(sum)
