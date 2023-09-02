T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floor = H
        num = N // H
    elif N % H != 0:
        floor = N % H
        num = N // H + 1
    print(floor * 100 + num)
