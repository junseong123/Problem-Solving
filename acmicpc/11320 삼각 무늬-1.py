t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if n > m:
        print(n // m + (n // m - 1) + (n // m - 2) + 1)
    elif n == m:
        print(1)
