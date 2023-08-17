N, K = map(int, input().split())
w = list(map(int, input().split()))
sum = 0
w.sort()
# for i in range(N):
#     print(w[i], end=" ")
# print(" ")
for _ in range(3):
    if len(w) >= 1:
        if min(w) + max(w) <= K:
            sum += 1
            w.remove(min(w))
            w.remove(max(w))
        else:
            w.remove(max(w))
    else:
        break
print(sum)