"""
쳅터: day 5
주제: 함수
문제:
두 개의 정수를 매개변수로 받아서, 두 수의 차를 반환하는 함수 subtract를 정의한다.
4, 8을 매개변수로 subject를 호출한 루 결과를 출력한다.
작성자:윤경환
작성일: 18 10 02
"""
# 두 수의 차를 반환하는subject 함수 정의 #
def subtract(a,b):
    #a: 첫번째 수
    #b: 두번째 수
    #반환값: 두 수의 차를 반환
    return a-b

#함수 호출
print(subtract(4,8)) #위치에 의해 인수(매개변수)가 전달됨
print(subtract(b=4,a=8)) #키워드 인수(매개변수)

a=10
b=True
c='김치'

print(type(a)) #변수의 타입을 반환하는 타입
print(type(b))
print(type(c))