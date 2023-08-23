word = input()
MOBIS = ["M", "O", "B", "I", "S"]
result = True
for i in MOBIS:
    if i not in word:
        result = False
        break

if result:
    print("Yes")
else:
    print("No")

# MOBIS = ["M", "O", "B", "I", "S"]
# word = input()
# result = True

# for i in MOBIS:
#     if i not in word:  # MOBIS가 없으면 False로 변경 후 break
#         result = False
#         break

# if result:
#     print("YES")
# else:
#     print("NO")
