# - 숫자 연산, 파일 입출력, 문자 입출력

### 거듭제곱(**)

`print(3**3)       # 27`

---

### 몫(//)

`print(10//3)       # 3`

---

### 나머지(%)

`print(10%3)        # 1`

---

### 나눗셈(/)

`print(3/5) # 0.6`

`type(3/5)    # float`

---

# 아스키코드로 출력

```python
a = input()

print(ord(a))
```

# 파일 입출력 with

## 파일 읽기

```python
file_path = "example.txt"

with open(file_path, 'r') as file:
		content = file.read()
		print(content)
```

---

## 파일 쓰기

```python
file_path = "example.txt"
content = "Hello, World!"
with open(file_path, 'w') as file:
 file.write(content)
```

# print

---

큰따옴표 3개 사이에 쓰면 한 줄 띄우고 그대로 출력

```python
print(
    """    8888888888  888    88888
   88     88   88 88   88  88
    8888  88  88   88  88888
       88 88 888888888 88   88
88888888  88 88     88 88    888888

88  88  88   888    88888    888888
88  88  88  88 88   88  88  88
88 8888 88 88   88  88888    8888
 888  888 888888888 88  88      88
  88  88  88     88 88   88888888"""
)
```

> sep=” “  : print문 안에 있는 인자들 사이에 특정한 구분값으로 분리해 출력.
> 

#인자들 사이는 쉼표 

```python
print(a, b, sep="")  # a b를 ab로 붙여줌
```

> end=” “ : print문 끝에 end에서 정의한 것을 출력 후 다음 줄이 연이어 출력.
> 

---

## 문자의 대, 소문자 변환

```python
S = input()
for i in S:
if i.isupper():
i = i.lower()
else:
i = i.upper()
print(i, end='')
```

`int(input())`

`map(int, input().split())`
