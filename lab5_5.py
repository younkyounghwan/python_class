"""
쳅터: day 5
주제: 함수
문제:

작성자: 윤경환
작성일: 18 10 04
"""

"""
l 변수에 [4,7,9,11,-5]를 저장한다.
l에서 최소값을 출력한다.
"""

l=[4,7,9,11,-5] #iterable한 값
print(min(l)) #min의 첫번째 매개변수는 iterable한 값을 넘긴다.
print(max(l))

print("----------------1")

"""
E: fruit 변수에 'apple','orange', 'banana'를 tuple로 배정한다.
F: fruit에서 최소값과 최대값을 출력한다.
"""

fruit = ('apple','orange', 'banana')
print(min(fruit))
print(max(fruit))

print("----------------2")

"""
G: friutd의 orange를 Orange로 변경한다.
H: friut에서 최소값과 최대값을 출력한다.
"""

fruit = ('apple','Orange', 'banana')
print(min(fruit))
print(max(fruit))

print("----------------3")

"""
I: 대소문자를 구분하지 않고 최대, 최소를 얻기 위해
min, max함수의 마지만 key매개변수로 str, lower(모두 소문자로 바꾸어 비교)를 전달한다.
(min(friut, key=str.lower))
"""

fruit = ('apple','Orange','banana')
print(print(min(fruit,key=str.lower)))
print(print(max(fruit,key=str.lower)))

print("----------------4")
"""
K: 1부터 50까지의 수 중 최대, 최소값을 출력한다.(range이용, min(range(1,50)))

"""
print(min(range(1,50)))
print(max(range(1,50)))

print("----------------5")
"""
L: min함수에 직접 1,3,6 값을 전달하여 최소값 출력
"""
print(min(1,3,6))