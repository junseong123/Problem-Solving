n = int(input())
a, b = map(int, input().split())
a //= 2
if n > a + b:
    print(a + b)
elif n <= a + b:
    print(n)
