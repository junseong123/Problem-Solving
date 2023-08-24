A = []
for i in range(3):
    A.append(list(map(int, input().split())))  # i= 1,2,3 =>A,B,C
print(A[0])
for i in range(3):
    if A[i][5] >= A[i][2]:
        A[i][5] -= A[i][2]
    elif A[i][5] < A[i][2]:
        A[i][5] += 60
        A[i][4] -= 1
        A[i][5] -= A[i][2]
    if A[i][4] >= A[i][1]:
        A[i][4] -= A[i][1]
    elif A[i][4] < A[i][1]:
        A[i][4] += 60
        A[i][3] -= 1
        A[i][4] -= A[i][1]
    if A[i][3] >= A[i][0]:
        A[i][3] -= A[i][0]
for i in range(3):
    print(A[i][3], A[i][4], A[i][5])
