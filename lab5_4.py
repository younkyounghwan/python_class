"""
쳅터: day 5
주제: 함수
문제:
4. 이름, 학번, 학과를 매개변수로 받아서 이를  출력하는 함수 print_me 함수를 정의한다.
이때, 학과가 매개변수로 넘어오지 않으면, "소프트웨어공학과"를 default 값으로 한다.
작성자: 윤경환
작성일: 18 10 04
"""

def print_me(name,no,method="소프트웨어공학과"):
    print(name,no,method)

print_me("윤경환",201814099)