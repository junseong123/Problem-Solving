N = int(input())
s = N

for i in range(1, N):
    print(" " * (N - i) + "*" * i)
for i in range(0, N + 1):
    print(" " * i + "*" * s)
    s -= 1
