"""
쳅터: day 5
주제: 함수
문제:

작성자: 윤경환
작성일: 18 10 04
"""

"""
B: 1에서 30까지의 합  출력 sum(range(1,31))
"""
print(sum(range(1,31)))
"""
c: 1, 3, 5, 7을 list로, tuple로, set으로 전달하여 합 출력
"""
l = [1,3,5,7]
t = (1,3,5,7)
s = {1,3,5,7}
print(sum(l))
print(sum(t))
print(sum(s))

"""
D: 50에 1,3,5,7의 합을 더하여 출력
"""

print(sum(l,50))