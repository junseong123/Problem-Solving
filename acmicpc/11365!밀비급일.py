l = []
sum = 0
while input == "END":
    l.append(input())
    sum += 1

for i in range(sum):
    print(l[i][::-1])
