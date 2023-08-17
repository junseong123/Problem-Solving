K, N, S = map(int, input().split())
print(K * N - S if K * N > S else 0)  # 이것은 if문을 한줄로 쓴 것이다.
