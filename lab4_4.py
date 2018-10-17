"""
쳅터: day 4
주제: 조건문(elif 이용)
문제:
1. l에 [3,5,6,8]을 배정한다.
2. l이 빈 리스트이면, "빈 리스트입니다." 아니면 l의 요소들을 출력하라.
3. 사용자로부터 출력하고 싶은요소의 인덱스를 입력받는다.
4. 인덱스 값이 이스트의 범위를 벗어나면, "해당 요소는 없습니다." 를 출력하고. 해당 인덱스가 있는 경우. 해당 요소를 출력한다.

작성자: 윤경환
작성일: 18.09.18
"""

# l에 [3,5,6,8]을 배정한다.
l= [3,5,6,8]
# l이 빈 리스트이면, "빈 리스트입니다." 출력
if not l:
    print("빈 리스트 입니다.")
# 아니면, l의 요소들을 출력하라.
else:
    print(l)
# 사용자로부터 출력하고 싶은요소의 인덱스를 입력받는다.
n=int(input("요소의 인덱스:"))
# 인덱스 값이 리스트의 범위를 벗어나면, (리스트릐 길이를 이용하여 비교)
if (n>=len(l)):
# "해당 요소는 없습니다."를 출력
    print("해당 요소는 없습니다.")

# 해당 인덱스가 있는 경우, 해당 요소를 출력한다.
else:
    print(l[n])