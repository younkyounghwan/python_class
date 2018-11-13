"""
쳅터: day6
주제ㅣ class , 상속계승
문제: shape, circle, rectangle class define

작성자 윤경환
작성일 18 11 13

"""
"""
1. shape class를 정의한다. method로 area(), perimeter()를 가지고 있다.
2. area는 면적, perimeter는 둘레를 반환한다. 하지만, shape class는 0을 반환한다.
3. __str__()를 정의한다. "도형"을 반환

4.shape를 계승하는 , Circle, rectangle class, triangle를 정의한다. __init__(), area(), perimeter()
    __str__()를 정의한다. Triangle의 __init()는 세변(첫번째 변은 빝변)과 높이를 매개변수로 받는다.
5. Circle class에는 getRadius() method를 정의한다.(반지름) 클래스 변수 pi = 3.1415로 정의한다.
6. Triangle, rectangle class에는 getHeight() method를 정의한다.(높이)
7. triangle, rectangle class에는 getWidth() method를 정의한다.(밑변)
8. triangle, rectangle class에는 변의 길이를 list형태로 반환하는 getSides() method를 정의한다. (변들을 반환)
 (변들을 반환, 삼각형 세변, 직사각형 네변)
"""

"""
실행부
1. s 변수는 도형이다.
2. 반지름이 5인 원을 정의하여 c변수에 저장한다.
3. 가로 세로가 5 10 인 직사각형을 정의하여 r에 저장한다.
4. 세변이 3(밑변), 4, 5인 삼각형을 정의하여 t에 저장한다.
5. c의 면적과 둘레를 출력한다.
6. r의 면적과 둘레를 출력한다.
7. t의 면적과 둘레를 출력한다.
8. t의 변들을 리스트로 받아 출력한다.
9. list l를 정의하여 s, c, r, t를 요소로 추가한다.
10. l의 각 요소에 대해, 해당 요소를 출력하고, 면적과 둘레를 계산하여 출력한다.
11. *test in for* getRadius() method를 수행한다. (오류발생)
"""
class shape:

    def area(self):


    def perimeter(self):

    def __str__(self):
        s = "도형"
        return "{}".format(s)


class Circle:
    def __init__(self,r,pi=3.1415):
        self.r = r
        self.pi = pi
    def area(self):

    def perimeter(self):



class Rectangle:
    def __init__(self,n,d):
        """

        :param n: 밑변
        :param d: 높이
        """
        self.n = n
        self.d = d
    def area(self):
    def perimeter(self):

    def getHeight(self):

    def getWidth(self):
    def getSides(self):

class Triangle:
    def __init__(self,n,d):
        """

        :param n: 밑변
        :param d: 높이
        """
        self.n = n
        self.d = d
    def area(self):
    def perimeter(self):
    def getHeight(self):

    def getWidth(self):

    def getSides(self):