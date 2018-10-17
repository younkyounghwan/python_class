"""
쳅터: day 5
주제:lambda함수의 리스트
작성자: 윤경환
작성일: 18 10 10
"""

l = [lambda x: x++2,
     lambda x: x++3,
     lambda x: x++4]

for f in l:
    print(f(3))

