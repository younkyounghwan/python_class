"""
쳅터: day 3
주제: set
작성일: 18.09.13
작성자: 윤경환
"""
s = {7,8,9,7} #set은 순서 의미 없음. 중복은 허용하지 않는다.
fruits = {'a': '사과', 'b': '배', 'c': '복숭아', 'd': '딸기'}
print(s)

#dictionary를 set으로 변환하기
print(set(fruits)) #key값만 set으로 변환된다.

#[3,4,5]를 set으로 형변환하여 s에 저장하고, 이를 출력한다.
print(set([3,4,5]))

#인덱스를 사용할 수 없음. 위치가 의미 없으므로
s.add(10)
print(s)

#remove로 삭제
s.remove(10)
print(s)

#정렬한 경과가 넘어옴
print(sorted(s))
