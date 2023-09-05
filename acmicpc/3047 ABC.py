x = list(map(int, input().split()))
y = []
p = input()

for i in range(3):
    if p[i] == "A":
        print(min(x), end=" ")
        x.remove(min(x))
    elif p[i] == "C":
        print(max(x), end=" ")
        x.remove(max(x))
    else:
        b = x
        print(b[0], end=" ")
