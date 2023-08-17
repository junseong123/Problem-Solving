N, A, B = map(int, input().split())
if B < A:
    print("Subway")
elif B > A:
    print("Bus")
else:
    print("Anything")
