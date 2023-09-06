L, R, A = map(int, input().split())
for i in range(A):
    if L < R:
        L += 1
    elif L > R:
        R += 1
    else:
        L += 1
print(min(L, R) * 2)
