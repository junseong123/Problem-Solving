while True:
    S = input("")
    if S == "#":
        break
    sum=0
    for i in S:
        if i in "aeiouAEIOU":
            sum += 1
    print(sum)
