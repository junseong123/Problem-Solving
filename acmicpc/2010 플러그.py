N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
    if a[i] > 1000:
        break
    if i != (N - 1):
        a[i] -= 1
print(sum(a))
