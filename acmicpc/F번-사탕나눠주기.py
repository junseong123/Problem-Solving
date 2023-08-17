# T-X = T점을 받은 학생의 사탕갯수  T는(T>X)
# 총 사탕갯수 = K
# 학생 명수 = N

N, K = map(int, input().split())
T = list(map(int, input().split()))
T.sort()

sum = T[3] - T[2]
K = K - sum
print(T[2] - (K // 2))