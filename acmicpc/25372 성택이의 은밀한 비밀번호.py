a = []
for i in range(int(input())):
    a.append(input())
    len_a = len(a[i])
    if len_a >= 6 and len_a <= 9:
        print("yes")
    else:
        print("no")
