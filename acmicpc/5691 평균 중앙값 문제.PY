# 0 두 개를 입력할 때까지 반복
while True:
    # A, B를 입력받음
    A, B = map(int, input().split())

    # A, B가 모두 0이면
    if A == 0 and B == 0:
        # 반복문을 탈출
        break
    # 입력값이 0이 아니면
    else:
        # A, B, C의 평균과 중앙값이 같을 때 가장 작은 수 C를 찾아야 하므로
        # C는 A보다 작으면서
        # B와 A의 차이값을 구해서 C도 A보다 그 차이만큼 작으면 됨
        print(A - (B - A))
