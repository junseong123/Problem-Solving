ch1 = [1, 1, 2, 2, 2, 8]
ch2 = [int(i) for i in input().split()]
ch3 = [str(ch1[i] - ch2[i]) for i in range(6)]
for i in ch3:
    print(i, end=" ")
