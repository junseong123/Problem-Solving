A, B = map(int, input().split())
K, X = map(int, input().split())

if A > (K - X) and (K + X) <= B and A <= K and B >= K:
    print(K + X - A + 1)
elif A <= (K - X) and (K + X) > B:
    print(B - (K - X) + 1)
elif A <= (K - X) and (K + X) <= B:
    print((K + X) - (K - X) + 1)
elif A > (K - X) and (K + X) > B and A <= K and B >= K:
    print(B - A + 1)
else:
    print("IMPOSSIBLE")
