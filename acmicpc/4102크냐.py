for i in range(1000):
    a, b = map(int, input().split())
    if a > b:
        print("Yes")
    if a < b:
        print("No")
    if a == b and a == 0:
        break
