k = []                              # 빈 리스트 생성
for i in range(9):                  # 9번 반복
    k.append(int(input()))          # append로 리스트에 요소 추가
    										            #  [3,29,38,12,57,74,40,85,61]
for index, num in enumerate(k):     # enumerate로 인덱스와 요소를 같이 가져옴
    if num == max(k):               # 만약 요소가 최댓값이면
        print(max(k))                       # max로 최댓값 출력
        print(k.index(max(k))+1)            # index로 최댓값의 인덱스 출력스 출력
print(k.index(85))                  # index로 85의 인덱스 출력