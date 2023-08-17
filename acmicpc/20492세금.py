N = int(input())

a = N - (N // 100 * 22)
b = N - ((N // 100 * 20) * 22 // 100)
print(a, b)
