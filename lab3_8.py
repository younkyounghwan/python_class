"""
쳅터: day 3
주제: dictionary(특징: nutable, key와 value의 쌍으로 구성됨)
작성일: 18.09.13
작성자: 윤경환
"""

#fruits = {'a': '사과', 'b': '배', 'c': '복숭아', 'd': '딸기'}
fruits = {'a': '사과', 'b': '배', 'c': '복숭아', 'd': '딸기'}
print(fruits)

#키가 'a'인 경우의 값을 출력하라.
print(fruits['a'])

#get() 함수는 키가 존재하지 않는 경우, none를 반환
print(fruits.get('k'))

#키가 'b'인 경우의 값을 '체리'로 수정하여라
fruits['b'] = '체리'
print(fruits)

#키가 'f'인 값 '아보카도'를 추가하여라.
fruits['f'] = '아보카도'
print(fruits)

#fruits에서 키가 'a;인 경우릐 값의 길이를 출력하라.
print(len(fruits['a']))

#모든 key 출력
print(fruits.keys())
#모든 value출력
print(fruits.values())
print("ㅇㄴㅇㄴ")
#friuts 안에 'a'라는 키가있으면 true, 없으면 false를 출력하라.
print('a' in fruits)
print('체리' in fruits) #in은 key값에 존재하는지에 대한 boolena 값. 체리는 key가 아님.
print('a' in fruits.keys())

#friuts 안에 value 중에 '복숭아'가 있으면 true, 없으면 false를 출력하라.
print('복숭아' in fruits.values())
print("ㅇㄴㅇㄴ12")

f= sorted(fruits) #key 순서에 따라 정렬된 key의 list를 반환
print(fruits)
print(f)
print("ㅇㄴㅇㄴ")

# vlaue를 정렬된 순서의 list로 출력
fv= sorted(fruits.values())
print(fv)
print("ㅇㄴㅇㄴ")

#key와 값을 튜플의 리스트로 만들어 출력하라. (.item())
print(fruits.items())
print("ㅇㄴㅇㄴ")

#삭제 (del 사용)
#'c'라는 키를 가지는 fruits를 삭제하라
del fruits['c']
print(fruits)
print("ㅇㄴㅇㄴ")
