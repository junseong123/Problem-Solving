num = list(map(int, input().split()))
while (
    num[0] != 0
    and num[1] != 0
    and num[2] != 0
    and num[0] < 30000
    and num[1] < 30000
    and num[2] < 30000
):
    num.sort()
    if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
        print("right")
    else:
        print("wrong")
    num = list(map(int, input().split()))
