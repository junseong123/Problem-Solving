a = []
for i in range(3):
    a.append(list(map(int, input().split())))

if a[0][0] == a[1][0]:
    x = a[2][0]
elif a[0][0] == a[2][0]:
    x = a[1][0]
elif a[1][0] == a[2][0]:
    x = a[0][0]
if a[0][1] == a[1][1]:
    y = a[2][1]
elif a[0][1] == a[2][1]:
    y = a[1][1]
elif a[1][1] == a[2][1]:
    y = a[0][1]
print(x, y)
