A = list(map(int, input().split()))
B = list(map(int, input().split()))
while True:
    if A[1] <= 0 or B[1] <= 0:
        break
    B[1] -= A[0]
    A[1] -= B[0]
if A[1] > 0:
    print("PLAYER A")
elif 0 < B[1]:
    print("PLAYER B")
elif A[1] <= 0 and B[1] <= 0:
    print("DRAW")
