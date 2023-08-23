N, X = map(int, input().split())

a = list(map(int, input().split()))
sum = []
for i in range(N - 1):
    sum.append((a[i] + a[i + 1]) * X)

print(min(sum))
