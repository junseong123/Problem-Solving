a = int(input())
b = int(input())
c = b / 100  # 백의 자릿수
d = (b - int(c) * 100) / 10  # 십의 자릿수
e = b - int(c) * 100 - int(d) * 10  # 일의 자릿수
print(a * e)
print(a * int(d))
print(a * int(c))
print(a * b)
