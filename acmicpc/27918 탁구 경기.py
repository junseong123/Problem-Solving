a = []
D, P = 0, 0
for i in range(int(input())):
    a.append(input())
    if (D - P) < 2 and (P - D) < 2:
        if a[i] == "D":
            D += 1
        else:
            P += 1
    else:
        break
print(D, P, sep=":")
