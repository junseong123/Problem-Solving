def shares(N, S):
    return S // (N + 1)


while True:
    try:
        N, S = map(int, input().split())
        print(shares(N, S))
    except EOFError:
        break
