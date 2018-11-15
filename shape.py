"""
쳅터: day6
주제ㅣ class , 상속계승
문제: shape, circle, rectangle class define

작성자 윤경환
작성일 18 11 13

"""
"""
1. Shape 클래스를 정의한다. 메쏘드로 area(), perimeter()를 가지고 있다.
A. area()는 면적, perimeter()는 둘레를 반환한다. 하지만, Shape 클래스는 0을 반환한다.
B. __str__()을 정의한다. “도형”을 반환
2. Shape를 계승하는, Circle, Rectangle 클래스, Triangle를 정의한다. __init()__, area(), perimeter()
, __str__()를 정의한다. Triangle의 __init__는 세변(첫번째 변은 밑변)과 높이를 매개변수로 받는다.
A. Circle 클래스에는 getRadius() 메쏘드를 정의한다.(반지름). 클래스변수 PI=3.1415로 정의한다.
B. Triangle, Rectangle 클래스에는 getHeight()메쏘드를 정의한다.(높이)
C Triangle, Rectangle 클래스에는 getWidth()메쏘드를 정의한다.(밑변)
D Triangle, Rectangle 클래스에는 변의 길이를 시계방향으로 list 형태로 반환하는 getSides() 메쏘드를 정의한다. (변들을 반환, 삼각형 세변, 직사각형 4변)
 __str__ 출력 예)
 <원> 반지름:5
 <직사각형> 밑변:5 높이:10
 <삼각형> 밑변:3 높이:4
 """

class Shape: #도형

    def area(self): #넓이
        return 0


    def perimeter(self): #둘레
        return 0

    def __str__(self): #__str__로 변수타입 변환
        self.name = "<Shape>" #도형
        s = self.name
        s = s + " 넓이: " + str(Shape.area(self)) + " 둘레: " + str(Shape.perimeter(self)) #출력 형식
        return "{}".format(s)


class Circle: #원
    def __init__(self,r,pi=3.1415):
        """

        :param r: 반지름
        :param pi: 3.1415
        """
        self.r = r
        self.pi = pi
        self.name = "Circle" #도형


    def area(self): #넓이

        return (self.r**2) * self.pi


    def perimeter(self): #둘레

        return 2 * self.r * self.pi

    def getRadius(self,pi=3.1415):
        self.pi = pi
        return pi

    def __str__(self): #__str__로 변수타입 변환


        s = ""
        s = s + "<" + str(self.name) +">" + " 넓이: " + str(Circle.area(self)) + " 둘레: " + str(Circle.perimeter(self))
        #출력 형식
        return "{}".format(s)




class Rectangle: #직사각형

    def __init__(self,n,d):
        """

        :param n: 가로
        :param d: 세로
        """
        self.n = n
        self.d = d
        self.name = "Rectangle" #도형
    def area(self): #넓이

        return self.n*self.d


    def perimeter(self): #둘레



        return 2 * (self.n + self.d)
    def getHeight(self):
        return self.d

    def getWidth(self):
        return Rectangle.area(self)

    def getSides(self):
        l = []
        l.append(self.d)
        l.append(self.n)
        l.append(self.d)
        l.append(self.n)
        return l
    def __str__(self): #__str__로 변수타입 변환

        s = ""
        s = s + "<" + str(self.name) + ">" + " 넓이: " + str(Rectangle.area(self)) + " 둘레: " + str(Rectangle.perimeter(self))
        return "{}".format(s)


class Triangle: #삼각형
    def __init__(self,n,m,o,d):
        """

        :param n: 밑변
        :param m: 변 1
        :param o: 변 2
        :param d: 높이
        """

        self.n = n
        self.m = m
        self.o = o
        self.d = d
        self.name = "Triangle"

    def area(self): #넓이

        return self.n * self.d / 2


    def perimeter(self): #둘레
        
        return self.n + self.m + self.o


    def getHeight(self):
        return self.d

    def getWidth(self):
        return Triangle.area(self)

    def getSides(self): #리스트 설정 후 각 변수 추가
        l = [] # 리스트
        l.append(self.n) #추가
        l.append(self.m)
        l.append(self.o)
        return l

    def __str__(self): #__str__로 변수타입 변환

        s=""
        s = s + "<" + str(self.name) + ">" + " 넓이: " + str(Triangle.area(self)) + " 둘레: " + str(Triangle.perimeter(self))

        return "{}".format(s)

"""
실행부
A. s 변수는 도형이다.
B. 반지름이 5인 원을 정의하여 c 변수에 저장한다.
C. 가로, 세로가 5, 10인 직사각형을 정의하여 r에 저장한다.
D. 세변이 3(밑변), 4, 5이고, 높이가 4인 삼각형을 정의하여 t에 저장한다.
E. c의 면적과 둘레를 출력한다.
F. r의 면적과 둘레를 출력한다.
G. t의 면적과 둘레를 출력한다.
H. t의 변들을 리스트로 받아 출력한다.
I. 리스트 l을 정의하여, s, c와 r을 요소로 추가한다.
J. l의 각 요소에 대해, 해당 요소를 출력하고, 면적과 둘레를 계산하여 출력한다.
K. for문 안에서 테스트: getRadius() 메쏘드를 수행한다.(오류 발생)
"""
s = Shape()
c = Circle(5)
r = Rectangle(5,10)
t = Triangle(3,4,5,4)
print(s)
print(c)
print(r)
print(t)
print(t.getSides())

l = []
l.append(s)
l.append(c)
l.append(r)

for i in range(0,3):
    print(l[i])
    #getRadius() #오류가 나므로 주석 처리

