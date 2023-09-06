N = list(map(int, input().split()))
count = 0
for i in range(len(N)):
    if N[i] > 0:
        count += 1
print(count)
