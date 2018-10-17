"""
쳅터: day4
주제: 문자열 함수
작성자: 윤경환
작성일: 18.09.06
"""

s="Test your Python debugging skills"
print(s.upper()) #대문자로 변환
print(s.lower()) #소문자로 변환

#문자열 안의 t의 갯수를 출력
print(s.count('t'))
print(s.count('T', 1)) #두번째 매개변수는 count 계산을 시작하는 위치

#사용자로부터 문자를 입력 받아, 대소문자 구문 없이 해당 문자의 개수를 출력
c=input("문자입력") #사용자로부터 문자 입력받기
print(s.count(c))
s1=s.upper() #비교되는 문자열을 대문자로 변환
#s에 저장된 문자열을 대문자로 변환하여 s1에 저장 - s에 저장된 문자열은 변동 없음

print(s)
print(s1)
print(s1.count(c.upper())) #비교되는 문자를 대문자로 변환하여 개수를 계산

#t가 있는 위치를 출력
print(s.index('t'))
print(s.index('t',4)) #두번째 매개변수는 검색 시작 위치
#index()함수는 찾으려는 문자가 없으면 오류 발생
#print(s.index('x'))
print(1231231)
# 대상 문자를 찾을 수 있는 또 다른 함수
print(s.find('t',6))
print(s.find('x')) #find() 함수는 찾으려는 문자가 없는 경우, -1을 변환

#scrip() 함수 테스트
print(s)
#왼쪽 공백 제거 후 출력
#오른쪽 공백 제거 후 출력
#양쪽 공백 제거 후 출력

#내용 바꾸기
#문장에서 python을 java로 바꾸어 출력
print(s.replace("Python","Java")) #replace가 s자체를 변동시키지는 않는다
print(s)

    #문장에섯 e를 i로 모두 바꾸어 출력
print(s.replace("e","i",1)) #3번째 매개변수는 변경할 최대 개수를 지정

#split 연습
#앞 뒤 공백을 제거한 후 빈칸을 기준으로 단어를 모두 나누기
print(s.strip().split(" "))
print(s.strip().split(" ",2)) #두개만 떼어 내기
# print(s.strip().split(" ",2).upper()) #split의 list는 문자열이 아니다.

#s의 길이 출력
print(len(s))

s="test"
s="kkk"
print(s)


s='''
kim
lee
park
'''
print(s)

c = input("문자열: ") #i의 데이터 타입은 문자열, input은 문자열을 반환하기 때문
c = int(input("문자열: ")) #i의 데이터 타입은 int, input은 문자열을 반환하기 떄문

j=100 #j는 int 타입
s1=str(j) #s1은 str타입
