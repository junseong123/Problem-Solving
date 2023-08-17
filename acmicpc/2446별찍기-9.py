N = int(input())
s = N - 1

for i in range(0, N - 1):
    print(" " * i + "*" * (2 * (N - i) - 1))
for i in range(1, N + 1):
    print(" " * s + "*" * (2 * i - 1))
    s -= 1
