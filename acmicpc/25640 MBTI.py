jinho = input()
a = []
count = 0
for i in range(int(input())):
    a.append(input())
    if jinho == a[i]:
        count += 1
print(count)
