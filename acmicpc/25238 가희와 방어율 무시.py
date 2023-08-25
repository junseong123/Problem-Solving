a, b = map(int, input().split())

if b == 0:
    if a >= 100:
        print(0)
    elif a < 100:
        print(1)
if b != 0:
    if a - (a * b / 100) >= 100:
        print(0)
    elif a - (a * b / 100) < 100:
        print(1)
