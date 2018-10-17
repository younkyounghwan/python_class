"""
쳅터: day 5
주제: 매개변수릐 전달 방식 비교(call-by-reference), 전역변수(global variable)
문제:
A. list를 받아서 마지막에 리스트의 요소의 개수를 요소로 추가하는 함수 addnum을 정의한다. 반환되는 값은 없다.
B. [5, 9, 14, 3]을저장하는 list를 변수 l를 정의한다.
C. l를 인수로 addnum함수를 호출한 후 l를 출력한다.

작성자: 윤경환
작성일: 18 10 10
"""

#배개변수의 수정 여부 확인을 위한 함수 정의
# call-by-reference 방식으로 매개변수 값을 전달

global_v = 100 #전역변수

def addnum(pl):
    global global_v
    global_v = 200
    pl.append(len(pl))


l=[5, 9, 14, 3]
addnum(l)
print(l)
print(global_v)