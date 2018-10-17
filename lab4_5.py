"""
쳅터: day 4
주제: 반복문(for문)
문제: 1에서 100까지 합을 구하여 출력하시오.
작성자:윤경환
작성일: 18 09 20
"""

sum = 0
for x in range(1,101):
    sum+=x

print(sum)

#1에서 100까지 3의 배수의 합을 구하여 출력하시오.

sum = 0
for x in range(1,101):
    if(x%3==0):
        sum+=x

print(sum)

sum = 0
for x in (1, 100 ,3):
    sum+=x

print(sum)



