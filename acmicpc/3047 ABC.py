x = list(map(int, input().split()))
y = []
p = input()

for i in range(3):
    if p[i] == "A":
        y.append(min(x))
        x.remove(min(x))
    elif p[i] == "C":
        y.append(max(x))
        x.remove(max(x))
    else:
        y.append(*x)
print(" ".join(map(str, y)))
