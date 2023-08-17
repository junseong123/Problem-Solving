N = int(input())
S = input()
sum = 0
for i in range(N):
    if S[i] in "aeiou":
        print(S[i], end="")
        sum += 1

print(sum)
