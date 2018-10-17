"""
쳅터: day 6
여러타입을 포함한 리스트
작성일:18.09.13
작성자 윤경환

"""

#l에 [1,2,[3,'john',4],'hi']를 저장한다.
l=[1,2,[3,'john',4],'hi']
#l에 3번째 요소를 출력한다.
print(l)

#l의 2번째 요소를 출력한다.
print(l[2])

#2라는 값이 있는 위치 출력
print(l.index(2))

#l의 2번째 요소의 1번째 요소를 출력한다.
print(l[2][1])

#l의 2번째 요소의 2번째 요소의 앞의 세글자만 출력한다.
print(l[2][1][0:3])

# in 연산 연습
print(2 in l)

#l에 3이 있으면 true 아니며, false를 출력하라.
print(3 in l)

#l의 2번째 요소안에 3이 있으면 true 아니면, false를 출력하라.
print(3 in l[2])

l[1]=8 #nutable 하다. list는 nutable한 데이터 타입이다.
print(l)

