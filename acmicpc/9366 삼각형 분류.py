T = int(input())
a = []
for i in range(1, T + 1):
    a, b, c = sorted(map(int, input().split()))
    if a == b == c:
        print(f"Case #{i}: equilateral")
    elif a == b or c == a or b == c:
        print(f"Case #{i}: isosceles")
    else:
        if b**2 + a**2 == c**2:
            print(f"Case #{i}: scalene")
        else:
            print(f"Case #{i}: invalid!")
