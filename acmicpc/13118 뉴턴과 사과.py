p = []

p = list(map(int, input().split()))
x, y, z = map(int, input().split())
k = 0
for i in range(4):
    if p[i] == x:
        k = i + 1

print(k)
