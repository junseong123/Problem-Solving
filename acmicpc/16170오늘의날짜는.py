import datetime  # datetime 모듈을 불러옴

date = datetime.datetime.now()  # 현재 날짜와 시간을 구함
print(date.year)  # 현재 연도 출력
print(date.month)  # 현재 월 출력
print(date.day)  # 현재 일 출력
print(date)  # 현재 날짜와 시간 출력
print(date.strftime("%Y\n%m\n%d"))  # 현재 날짜를 YYYY-MM-DD 형식으로 출력
