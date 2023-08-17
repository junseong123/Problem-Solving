a = [int(input()) for _ in range(28)]  # 28개의 숫자를 입력받아서 리스트에 저장
b = [i for i in range(1, 31)]  # 1부터 30까지의 숫자를 리스트에 저장

for i in range(28):  # 28개의 숫자를 입력받았으므로 28번 반복
    b.remove(a[i])  # 입력받은 숫자를 리스트에서 제거
for i in b:  # 리스트에 남아있는 숫자 출력
    print(i)
