n = int(input())

for i in range(1, n + 1):
    if n == 1:
        print("*")
        break
    if i == 1:
        print((n - 1) * " " + "*")
    elif i == n:
        print("*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
