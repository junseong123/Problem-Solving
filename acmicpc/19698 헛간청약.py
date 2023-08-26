N, W, H, L = map(int, input().split())

if ((W // L) * (H // L)) <= N:
    print((W // L) * (H // L))
else:
    print(N)
