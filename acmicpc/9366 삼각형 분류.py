T = int(input())
a = []
for i in range(1, T + 1):
    a, b, c = sorted(map(int, input().split()))
    if a + b <= c:
        print(f"Case #{i}: invalid!")
    elif a == b == c:
        print(f"Case #{i}: equilateral")
    elif a == b or c == a or b == c:
        print(f"Case #{i}: isosceles")
    elif b != a != c:
        print(f"Case #{i}: scalene")

# 삼각형의 결정조건 : 짧은변의 길이의 합 > 긴변
