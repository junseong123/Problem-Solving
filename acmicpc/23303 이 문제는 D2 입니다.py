N = input()
naver = "unrated"
for i in range(0, len(N) - 1):
    if (N[i] == "d" or N[i] == "D") and N[i + 1] == "2":
        naver = "D2"


print(naver)
