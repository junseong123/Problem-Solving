N = int(input())
A, B, C = map(int, input().split())
sum = 0

if A <= N:
    sum += A
elif A > N:
    sum += N
if B <= N:
    sum += B
elif B > N:
    sum += N
if C <= N:
    sum += C
elif C > N:
    sum += N

print(sum)
