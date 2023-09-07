T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    if N < 12:
        print(-1)
    else:
        print(11 * M + 4)
