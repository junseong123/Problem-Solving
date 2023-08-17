number = int(input())
for i in range(1, number + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")
