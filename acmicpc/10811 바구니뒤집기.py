n, m = map(int, input().split())

bucket_list = [i for i in range(1, n + 1)]
# 1부터 n까지의 숫자를 리스트로 만듦
# 인덱스 자체는 0번부터 시작하므로 i - 1부터 j까지 뒤집는다.
# 인덱스 i - 1번을 지정해줘야한다.
# j번까지 뒤집기 위해서는

for _ in range(m):
    i, j = map(int, input().split())
    bucket_list[i - 1 : j] = bucket_list[i - 1 : j][::-1]

print(*bucket_list)
