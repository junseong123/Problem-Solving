import sys

sum = 0
for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    sum = a + b
    print(sum)
