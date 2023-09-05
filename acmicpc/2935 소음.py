a = []
for i in range(3):
    a.append(input())
if a[1] == "+":
    print(int(a[0]) + int(a[2]))
if a[1] == "*":
    print(int(a[0]) * int(a[2]))
