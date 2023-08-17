S = input()  # S = 'aBcD'
for i in S:  # i = 'a'
    if i.isupper():  # i = 'a' -> False
        i = i.lower()  # i = 'a'
    else:  # i = 'a' -> True
        i = i.upper()  # i = 'A'
    print(i, end="")  # print('A', end='')
