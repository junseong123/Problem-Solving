N = input()
naver = "unrated"
for i in range(len(N)):
    if (N[i] == "d" or N[i] == "D") and N[i + 1] == "2":
        naver = "D2"
        break

print(naver)
