# 입력
a, b, c = map(int, input().split())
order = input()

# 오름차순 정렬
a, b, c = sorted((a, b, c))

# 순서대로 출력
for i in order:
    if i == "A":
        print(a, end=" ")
    elif i == "B":
        print(b, end=" ")
    else:
        print(c, end=" ")
