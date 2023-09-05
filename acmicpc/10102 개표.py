v = int(input())
n = input()
a, b = 0, 0
for i in range(len(n)):
    if n[i] == "A":
        a += 1
    elif n[i] == "B":
        b += 1
if a == b:
    print("Tie")
elif a > b:
    print("A")
else:
    print("B")
