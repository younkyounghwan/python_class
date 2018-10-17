"""
쳅터: day 5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제:
A. 팩토리얼 계산 함수 fact를 재귀한수로 정의하여, fact(5)를 호출한 결과를 출력하라
작성자: 윤경환
작성일: 18 10 10
"""

def fact(a): #팩토리얼
    if a == 1: #a가 1일때
        return a #a반환
    else: #아닐때
        return a*fact(a-1) #재귀함수 사용

print(fact(5)) #출력