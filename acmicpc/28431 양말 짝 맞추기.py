a = []
for i in range(5):
    a.append(int(input()))

b = list(set(a))
for i in b:
    if a.count(i) % 2:
        print(i)
