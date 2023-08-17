a = input()

if len(a) == 2:
    print(int(a[0]) + int(a[1]))
elif len(a) == 3:
    if a[1] == "0":
        print(int(a[0]) * 10 + int(a[2]))
    elif a[2] == "0":
        print(int(a[0]) + int(a[1]) * 10)
elif len(a) == 4:
    print(int(a[0]) * 10 + int(a[2]) * 10)
