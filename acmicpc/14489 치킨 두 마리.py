A, B = map(int, input().split())
Chicken = int(input())
if A + B >= Chicken * 2:
    print(A + B - Chicken * 2)
else:
    print(A + B)
