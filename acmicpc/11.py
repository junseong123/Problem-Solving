fruits = ["용과", "포도", "석류"]
people = ["은태", "남주", "미녀"]
for idx, (fruit, person) in enumerate(zip(fruits, people)):
    if idx == 1:
        continue

print(f"{person}는 {fruit}를 좋아해~")
