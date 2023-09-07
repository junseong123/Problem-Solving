T = int(input())
a = []
for i in range(T):
    a, b, c = map(int, input().split())
    if a == b == c:
        print(f"Case #{i+1}: equilateral")
    elif a == b or c == a or b == c:
        print(f"Case #{i+1}: isosceles")
    else:
        if (a + b + c - max(a, b, c) - min(a, b, c)) ** 2 + min(a, b, c) ** 2 == max(
            a, b, c
        ) ** 2:
            print(f"Case #{i+1}: scalene")
        else:
            print(f"Case #{i+1}: invalid!")
