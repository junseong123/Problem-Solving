n = input()
sum = 0
for i in range(len(n)):
    if n[i] in "aeiou":
        sum += 1
print(sum)
