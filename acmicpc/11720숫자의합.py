N = int(input())
x = []
sum = 0
x = list(map(int, input()))
for i in range(0, N):
    sum += x[i]
print(sum)
