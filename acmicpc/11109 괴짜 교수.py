n = int(input())
for i in range(n):
    d, n, s, p = map(int, input().split())
    if n * s > p * n + d:
        print("parallelize")
    elif n * s < p * n + d:
        print("do not parallelize")
    else:
        print("does not matter")
