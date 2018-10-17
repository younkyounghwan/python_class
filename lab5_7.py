"""
쳅터: day 5
주제: 함수
문제:

작성자: 윤경환
작성일: 18 10 04
"""

def modify(n):
    n +=1
    return n
#실행 시작 부분
k=10 #변수 정의
print("k =",k) #호출 전 변수 값 출력
re = modify(k) #modify호출 후 결과 값을 re에 저장
print("k =",k) #호출 후 변수 값 출력
print("re =",re)

#코드에 서로 영향이 없을 때, call-by-value, 독립적