"""
쳅터: day 5
주제: 함수
문제:
문자열이 몇 개 들어올 지 예상할 수 없다고 가정하자. 여러개의 문자열을매개변수로받아서, 해당 문자열들을 ','로 연결하여
출력하는 함수 print_string을 재정의한다. (책 p139참고 매개변수 앞에 *붙이기)
사과, 오랜지, 딸기를 매개변수로 해서 print_string을호출한다.
작성자:윤경환
작성일: 18 10 02
"""

#print_string 함수 정의
def print_string(*a):
    for i in a:
        print(i,end=", ")
#매개변수 앞에 *을 사용하기 연습

#실행 코드 시작
#매개변수를 튜플로 만들지 말고, 세개의 문자열을 직접 매개변수로 넘긴다.
print_string("apple","orange","strawberry")