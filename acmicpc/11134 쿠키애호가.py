T = int(input())
for i in range(T):
    N, C = map(int, input().split())
    print(N // C if N % C == 0 else N // C + 1)
