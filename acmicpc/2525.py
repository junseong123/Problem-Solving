H, M = map(int, input().split())
timer = int(input())

h = timer // 60
m = timer % 60

H += h
M += m

if H >= 23:
    H -= 24
if M >= 59:
    M -= 60
    H += 1

print(H, M)
