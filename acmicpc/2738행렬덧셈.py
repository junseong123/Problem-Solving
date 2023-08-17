# N, M = map(int, input().split())

# arr = []
# arr_1 = []
# for i in range(2):
#     arr.append([])  # 새로운 내부 배열 선언
#     for j in range(M):
#         arr[i].append(input().split())


# for j in range(M):
#     print(arr[0][j] + arr[1][j])

# n, m = map(int, input().split())

# a, b = [], []

# for i in range(n):
#     i = list(map(int, input().split()))
#     a.append(i)

# for i in range(n):
#     i = list(map(int, input().split()))
#     b.append(i)

# for i in range(n):
#     for j in range(m):
#         print(a[i][j] + b[i][j], end = " ")
#     print()
# --------------------------------------------------
n, m = map(int, input().split())
a, b = [], []
for i in [a, b]:
    for j in range(n):
        i.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(*a[i])
