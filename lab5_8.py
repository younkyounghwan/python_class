"""
쳅터: day 5
주제: 함수
문제:

작성자: 윤경환
작성일: 18 10 04
"""

#매대변수의 수정 여부 확인을 위한 하수 정의
#call-by-value 방식으로 매개변수 값을 전달
#매개변수 값을 복사(copy)하여 전달

def modify(s):
    s+=" to you"
    return s

msg = "Happy Birthday"
print("호출 전 msg =",msg)
re=modify(msg)
print("호출 후 msg =",msg)
print("re=",re)