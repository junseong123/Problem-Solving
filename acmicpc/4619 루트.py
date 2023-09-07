while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break
    A1 = int(B ** (1 / N))

    if abs(A1**N - B) >= abs((A1 + 1) ** N - B):
        print(A1 + 1)
    else:
        print(A1)
