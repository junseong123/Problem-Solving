L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
a1 = A // C
b1 = B // D
if A % C != 0:
    a1 += 1
if B % D != 0:
    b1 += 1
if a1 > b1:
    print(L - a1)
else:
    print(L - b1)
