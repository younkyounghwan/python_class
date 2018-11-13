"""
쳅터ㅣ day6
주제: calss, 상속/계승(inheritance), 객체지향 (object - oriented programming)
문제: 정수집합 클래스

작성자: 윤경환
작성일 18 11 08
"""
"""
1. 사람 클래스를 정의한다. 이름과 나이를 (data) attribute로 가지고 있다.
A. 이름과 나이를 매개변수로 받는 생성자가 있다.
B. 나이를 1살 더하는 getOlder 메쏘드가 있다.
C. 문자열 반환, 프린트 method
"""

# 실행부
#두 명의 Person instance를 만들어서 나이를 한살 올린 후 출력한다.
class Person:
    #super class, parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getOlder(self):
        self.age +=1
    def __str__(self):
        s = ""
        s = s + "이름: " + self.name + " 나이: " + str(self.age)
        return "{}".format(s)
    def print(self):
        print(self)

"""
3. 사람을 계승하는 학생 클래스를 정의한다. 학교와 학년, 학번을 data attribute로 가지고 있다.
A. 이름, 나이, 학년, 학번을 받는 생성자가 있다. 생성자 내에서 사람의 생성자(Persion.__init__)를 호출한다.
B. 학년을 진급하는 upgrade() method가 있다.
C. 문자열 반환(override), print method
"""

class Student(Person): #Student 클래스는 Person클래스를 계승한다.
    #Person클래스와 Student클래스는 is_a관계
    #sub class
    def __init__(self,name , age, grade, snum):
        """
        이름 나이 학년 학번을 받는 생성자
        :param name:
        :param age:
        :param grade:
        :param snum:
        """
        """
        생성자 내에서 사람의 생성자(person.__init__)를 호출한다.
        Student도 일종의 Person이다.
        Person이라서 가지고 있는 attribute인 age와 name은
        Person의 생성자(__init__)를 통해 초기화한다.
        """
        Person.__init__(self, name, age)
        """
        학번과 학년은 Student의 생성자 내에서 초기화
       """

        self.grade = grade
        self.snum = snum
        self.school = "skhu"


    def upgrade(self):
        self.grade +=1
    def __str__(self):
        """
        Person class에서 정의된 __str__를 overriding한다.

        :return: 문자열
        """

    def __str__(self):
        s = Person.__str__(self) #Person class에 __str__를 먼저 호출한 후 문자열 연결 예정
        s = s + " 학교: " + self.school + " 학년: " + str(self.grade) + " 학번: " + str(self.snum)
        return "{}".format(s)

    def print(self):
        """
        Person class에서 정의된 print()를 재정의한다.
        :return:
        """
        print(self)

p1 = Person("홍길동",20)
p2 = Person("임꺽정",21)
#p1.upgrade() #p1은 Student가 아니므로, upgrade() method를 사용할 수 없다.
p1.getOlder()
p1.print()
p2.print()

# 두 명의 Student instance를 만든다.
s1 = Student("김삼수", 20, 2,20182323)
s2 = Student("김사수", 21, 3,20185323)
s1.getOlder() #s1은 Student인데, Person을 계승했으므로 Person의 method 사용이 가능하다.
s1.upgrade()
s1.print()

l = [p1,p2,s1,s2]
for e in l:
    e.getOlder()
    e.print()