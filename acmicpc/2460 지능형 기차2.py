sum = 0
max = 0
for i in range(10):
    a, b = map(int, input().split())
    sum += -a + b
    if max < sum:
        max = sum
print(max)
