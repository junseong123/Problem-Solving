a = int(input())
b = int(input())
c = int(input())
sum = a + b + c

if sum == 180:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    elif a != b or a != c or b != c:
        print("Scalene")
else:
    print("Error")
