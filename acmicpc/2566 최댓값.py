a = []
max = 0
for i in range(9):
    a.append(list(map(int, input().split())))

for q in range(9):
    for w in range(9):
        if a[q][w] > max:
            max = a[q][w]
            x = q
            y = w
print(max)
print(x + 1, y + 1)
print(a[2][1])
