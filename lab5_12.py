"""
쳅터: day 5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제:
A. 곱하기를 더하기 반복문으로 구현한 함수 prod를 정의하여 prod(3,6)를 계산하여 출력
작성자: 윤경환
작성일: 18 10 10
"""

def prod(a,b):
    r=0
    for i in range(0,b):
       r+=a
    return r

def r_prod(a,b):
    if b==1:
        return a
    else:
        return 3*r_prod(a, b-1)

#재귀함수를 이용하여 구현한 함수 r_prod
print(prod(3,6))
print(r_prod(3,6))