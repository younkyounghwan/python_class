"""
쳅터: day 4
주제: 조건문(elif 이용)
문제: 사용자로부터 정수를 입력받는다.
        0보다 크면 "양수", 0이면 "0", 0보다 작으면 "음수"를 출력한다.
작성자: 윤경환
작성일: 18.09.18
"""

#정수 입력 받기
num=int(input("정수 입력:"))
#정수가 0보다 크면 양수 출력
if(num>0):
    print(num)
#그렇지 않고, 정수가 0이면 0 출력
elif(num==0):
    print(num)
#그렇지 않으면 음수 출력
else:
    print(num)