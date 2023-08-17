a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    # 그 외에 같은 경우
    print("==")
