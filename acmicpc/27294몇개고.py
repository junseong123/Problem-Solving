T, S = map(int, input().split())
if T <= 11:
    print(280)
elif 12 <= T and T <= 16:
    if S == 0:
        print(320)
    else:
        print(280)
elif 17 <= T:
    print(280)
