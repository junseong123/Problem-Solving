N = int(input())
sum, sum1, sum2 = 0, 0, 0
for i in range(1, N + 1):
    sum += i
    sum1 += i
    sum2 += i**3
print(sum)
print(sum1**2)
print(sum2)
