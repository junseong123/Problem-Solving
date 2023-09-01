A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    M = (B + C) % 60
    H = (A + (B + C) // 60) % 24
    print(H, M)

else:
    M = B + C
    H = A
    print(H, M)
