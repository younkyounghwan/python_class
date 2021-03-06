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
# 필요한 module을 수입하기
import shape #shape.py에 정의된 클래스, 함수등을 수입해서 사용하겠다는 의미 확장자는 붙이지 않는다.


s = shape.Shape() #shape.의 의미는 "shape.py"에서 정의된 의미
                # shape가 shape.py에 정의된 클래스임을 의미
c = shape.Circle(5)
r = shape.Rectangle(5,10)
t = shape.Triangle(3,4,5,4)
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

