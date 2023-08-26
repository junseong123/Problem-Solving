n = int(input())
cnt = 0
for i in range(n):
    d = int(input()[2:])
    if d <= 90:
        cnt += 1
print(cnt)
