N = int(input())
s = N

for i in range(1, N):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)
for i in range(0, N + 1):
    print("*" * s + " " * (2 * i) + "*" * s)
    s -= 1
