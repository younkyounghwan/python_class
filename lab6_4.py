"""
쳅터ㅣ day6
주제: calss, class variable, default 매개변수 operator overloading 복습
문제: 정수집합 클래스

작성자: 윤경환
작성일 18 11 06
"""
"""
student 클래스를 정의한다. 다음 학생에게 줄 학번을 클래스 변수 (class variable) tag로 정의한다.
메쏘드와 같은 레벨에서 변수를 정의하면 클래스 변수가 된다. self가 필요없다.
"""
class Student:
    tag = 1 #다음 학생에게 줄 학번, 모든 instance가 공유하여 사용. class variable(member)
    def __init__(self,name, grade=1):
        """
        이름, 학년을 매개변수로 받는다.
        grade는 학년을 매개변수로 받지 않는 경우, 1학년이 default다.
        """
        # 매개변수 값을 self 맴버 (instance variable)에 배정한다.
        self.name = name
        self.grade = grade
        # 클래스 변수인 tag값을 학번으로 배정
        self.snum =  Student.tag
        Student.tag += 1
    def __str__(self):

        s = "학번:"
        s = s + str(self.snum) + " 이름:" +self.name + " 학년:" +str(self.grade)
        return "{}".format(s)
    """
    Student 클래스에 학년을 올리는 upgrade()라는 method를 정의한다.
    self를 매개변수로 받는다. 몇 학년을 올릴지는 매개변수로 받는다. 1년 올리는 것이 default이다.

    """
    def upgrade(self,up=1):
        """
        진급시킨다. 4학년인 경우 진급시키지 말고, "%s는 졸업 예정 학생입니다."를 출력
        :param up:
        :return:
        """
        s = self.name
        if self.grade == 4:
            print("{}는 졸업 예정인 학생입니다.".format(s))
        else:
            self.grade = self.grade + up

    """
    Student 클래스에 __eq__ method를 정의한다. 학번을 비교하여 같은 학생이면 True, 아니면 False를 반환한다.

    """
    def __eq__(self, o):
        """

        :param o:  학생 instance
        :return: boolean
        """

        a = self.name
        b = o.name

        if a==b:
            return True
        else:
            return False
# 실행부 시작
# 학생 인스턴스 3개 생성
s1 = Student("김일수", 4)
s2 = Student("김이수", 2)
s3 = Student("김삼수")
print("===진급 전 출력===")
#3개의 학생 인스턴스 값을 출력
print(s1)
print(s2)
print(s3)

# s2의 학년을 1 학년 높힌다.(매개변수 안보내기)
s2.upgrade()

#s3의 학년을 2학년 높인다. (매개변수 보내기)
s3.upgrade(2)
print("\n==진급 후 출력===")
#진급 후의 학생 정보
print(s1)
print(s2)
print(s3)

#list에 3명의 학생 정보 저장
l=[]
l.append(s1)
l.append(s2)
l.append(s3)
l.append(Student("김사수")) # list의 요소를 직접 생성하여 배정

print("\n===리스트에 있는 요소 출력===")
for s in l:
    #진급시키기
    s.upgrade()  # list에 있는 요소의 데이터 타입이 Studnet이므로, Student의 method를 호출할 수 있다.

    print(s)

# s5 학생의 이름은 "김일수"로 생성
print("")
s5 = Student("김일수")
l.append(s5)
if (s1==s5):
    print("s1와 s5는 같은 학생입니다.")
else:
    print("s1과 s5는 다른 학생입니다.")

# s1과 s5가 같은 학생인지 조사하여 결과를 출력

# s6에 s1을 배정
# s6와 s1이 같은 학생인지 검사하여 결과를 출력
s6 = s1
if (s1==s6):
    print("s1와 s6는 같은 학생입니다.")
else:
    print("s1과 s6는 다른 학생입니다.")
l.append(s6)


#instance의 맴버를 외부에서 직접 수정할 수 있다.
#권장하지 않는다.
# instance의 member는 자신의 method에서 수정하는 것이 좋다.
#encapsulation
s1.name="이일수"
print(s1)