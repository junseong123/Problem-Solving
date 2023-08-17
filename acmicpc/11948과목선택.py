a, b = [], []
asum, bsum = 0, 0
for i in range(4):
    a.append(int(input()))
for i in range(2):
    b.append(int(input()))
for i in range(4):
    asum += a[i]
for i in range(2):
    bsum += b[i]
asum -= min(a)
bsum -= min(b)
print(asum + bsum)
