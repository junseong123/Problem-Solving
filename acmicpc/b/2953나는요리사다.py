n_list = []
for i in range(5):
    n_list.append(list(map(int, input().split())))
print(n_list)

sum_list = []
for i in range(5):
    sum_list.append(sum(n_list[i]))

max_sum = max(sum_list)
print(sum_list.index(max_sum) + 1, max_sum)
