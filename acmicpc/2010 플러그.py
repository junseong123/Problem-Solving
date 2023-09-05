N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

    if i != (N - 1):
        a[i] -= 1
print(sum(a))
