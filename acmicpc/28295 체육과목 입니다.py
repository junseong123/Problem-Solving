n = []
sum = 0
for i in range(10):
    n.append(int(input()))
    if n[i] == 1:
        sum += 90
    if n[i] == 2:
        sum += 180
    if n[i] == 3:
        sum -= 90
sum = sum % 360
if sum == 0:
    print("N")
elif sum == 90:
    print("E")
elif sum == 180:
    print("S")
elif sum == 270:
    print("W")
