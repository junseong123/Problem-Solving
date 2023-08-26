x = int(input())
while True:
    length = len(str(x))
    k = x // (10 ** (length - 1))
    x = length * k
    if x == length * k:
        print("FA")
        break
    else:
        print("NFA")
