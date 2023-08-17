N = int(input())
s = N - 1

for i in range(0, N):
    print(" " * i + "*" * (2 * (N - i) - 1))
