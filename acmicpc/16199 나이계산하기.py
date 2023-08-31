a = list(map(int, input().split()))
b = list(map(int, input().split()))


if a[1] < b[1] or (a[1] == b[1] and a[2] <= b[2]):
    print(b[0] - a[0])  # 생일 지남
else:
    print(b[0] - a[0] - 1)  # 생일 안지남

print(b[0] - a[0] + 1)
print(b[0] - a[0])
