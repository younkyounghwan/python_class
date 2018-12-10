"""
쳅터: day 6
주제: class

문제: 좌표를 표현하는 클래스 coordinate를 정의한다.
1. __init__는 x,y좌표를 받아서 self의 x,y에 배정
2. c, 거리를 구하는 distance 메소드를 정의한다. self와 다른 좌표 other를 매개변수로 받는다.
거리는 (x좌표 사이의 차의 제곱(**2로 계산)과 y좌표 사이 차의 제곱의 합)의 제곱근이다. 제곱근(**0,5로 계산)


작성자: 윤경환
작성일: 18 10 18
"""


class coordinate():

    """
    좌표를 표현하는 클래스
    """
    def __init__(self,x,y):
        """

        :param x: x좌표값
        :param y: y좌표 값
        """

        self.x = x
        self.y = y

    def distance(self,other):
        """

        두 좌표의 거리를 계싼하여 반환
        :param other: 다른 좌표
        :return: self와 other와의 거리를 반환
        """


        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
# 실행 코드 시작
"""
실행 코드 부분
(3 ,4) 좌표의 점 c를 정의
원점 orgin 정의
(3, 4)와 원점과의 거리를 출력
"""
c= coordinate(3,4)
origin = coordinate(0,0)
c1 = coordinate(10,9)

print("거리: %.2f"%c.distance(origin)) #origin이 self, c가 other에 전달됨
print("거리: %.2f"%c1.distance(c)) #c1이 self c가 other에 전달됨
print("거리: %.2f"%coordinate.distance(c1, origin)) #클래스 이름과 함꼐 메소드 호출도 가능. 이 때는 self에 해당하는 매개변수를 보내야 한다.