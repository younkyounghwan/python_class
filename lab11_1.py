

"""
쳅터: day 6
주제: class

문제: 정수집합 클래스
1. intSet 클래스는 정수들의 집합이다. 정수들을 관리하는 리스트 self.vals를 애트리뷰트로 가진다.
2. 새로운 정수 e를 추가하는 insert메쏘드. 해당 요소가 이미 있다면 추가하지 않을 것
3. e가 정수집합에 초함되어 있는지 확인하는 메쏘드인 involve 정의(True, False 반환)
4. e를 제거하는 remove 메쏘드
5. 단, e가 해당 집합에 없다면 적단한 오류메세지를 출력
6. 집합 형식의 문자열로 변환시켜주는 __str__ 메쏘드. 단, 정수들은 정렬되어 반환되어야한다.

작성자: 윤경환
작성일: 18 11 1
"""
#실행부분
"""
A. inSet을 저장하는 변수 s를 정의
B. s에 insert를 이용하여 하나씩 5,3,7을 삽입
C. s를 정렬하여 출력
D. s에 8이 있는지 결과 출력
E. s에 3이 있는지 결과 출력
F. s에서 3을 제거
G. s에서 4를 제거
H. s를 정렬하여 출력

"""

class inSet():
    def __init__(self):
        self.vals = []
    def involve(self,e):
        for i in self.vals:
            if (i==e):
                return print(True)
        return print(False)
    def insert(self,e):
        self.vals.append(e)
    def remove(self,e):
        if self.involve(e):
            self.vals.remove(e)
        else:
            print("There is no < %s > in list" %e)

    def __str__(self):
        self.vals.sort()
        s='('
        s=s+str(self.vals)+')'
        return "{}".format(s)
s = inSet()
s.insert(5)
s.insert(3)
s.insert(7)
print(s)
s.involve(8)
s.involve(3)
s.remove(3)
s.remove(4)
print(s)






