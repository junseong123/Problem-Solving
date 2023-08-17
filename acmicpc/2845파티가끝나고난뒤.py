L, P = map(int, input().split())
A = list(map(int, input().split()))
B = [L * P] * 5
for i in range(5):
    B[i] = A[i] - B[i]
for i in range(5):
    print(B[i], end=" ")
