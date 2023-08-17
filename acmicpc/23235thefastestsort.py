i = 0
while True:
    i += 1
    a = [int(i) for i in (input()).split()]
    b = a[0]

    if a[0] == 0:
        break
    elif a != 0:
        a.remove(a[0])
        a.sort()
        print(f"Case {i}: Sorting... done!")


# cnt = 0

# while True:
#     if input() == "0":
#         break

#     else:
#         cnt = cnt + 1

#         fmt = f"Case {cnt}: Sorting... done!"

#         print(fmt)
