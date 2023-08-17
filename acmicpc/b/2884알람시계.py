H, M = map(int, input().split())

if M >= 45:
    M = M - 45
elif M < 45:
    if H == 0:
        H = 23
        M = 60 - abs(M - 45)
    elif H > 0:
        H = H - 1
        M = 60 - abs(M - 45)
print(H, M)
