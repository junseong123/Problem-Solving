N = int(input())
A = []
for i in range(N):
    A.append(input(""))

for i in range(N):
    print(i + 1, ". ", A[i], sep="")
