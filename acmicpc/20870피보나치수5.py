num = int(input())
qoduf = [0, 1]
for i in range(2, num + 1):
    qoduf.append(qoduf[i - 1] + qoduf[i - 2])
print(qoduf[num])
