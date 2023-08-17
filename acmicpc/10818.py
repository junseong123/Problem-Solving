a = int(input())

num_list = nums = list(map(int, input().split()))
max = num_list[0]
min = num_list[0]

for i in range(0, a):
    if max < i:
        max = i
    if min > i:
        min = i

print(min, max)
