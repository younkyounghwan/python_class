"""
쳅터: day 5
주제: lambda 함수
- 무명함수
- 매개변수를 받을 수 있다.
- 한줄 계산
- 반환값이 1개, 한줄계산의 결과가 반환값
문제:


작성자: 윤경환
작성일: 18 10 10
"""
#합을 구하는 lambda 함수(무명함수 no-named fiction)
sum = lambda x, y: x+y #lambda 함수의 시작값이 sum에 저장됨. 실행되는 건 아님.
k= sum(5,8) # lambda함수 호출
print(sum(5, 10)) #sum을 실행
print(k)
