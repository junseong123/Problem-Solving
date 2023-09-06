A = list(map(int, input().split()))
B = list(map(int, input().split()))
while True:
    if A[1] <= 0 or B[1] <= 0:
        break
    B[1] -= A[0]
    A[1] -= B[0]
if A[1] < 0:
    A[1] = 0
elif B[1] < 0:
    B[1] = 0
if A[1] > B[1]:
    print("PLAYER A")
elif A[1] < B[1]:
    print("PLAYER B")
else:
    print("DRAW")
