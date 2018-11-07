"""
쳅터: day 6
주제: class

문제:
숫자를 하나씩 발생시키는 counter 클래스 정의
작성자: 윤경환
작성일: 18 10 18
"""
#counter 클래스 정의
class Counter:
    def __init__(self,start=0):
        """
        instance를 생성할 때 초기화하는 메소드. instance를 생성할 때 자동 호출됨.
        python에서는 class당 하나의 __init__함수를 정의할 수 있음
        """
        self.count = start



    def reset(self):
        """
        카운터를 초기화하는 메소드
        self: method가 수행되는 instance 자신을 의미

        :return:
        """
        self.count = 0 #counter는 instance variable(member)

    def increment(self):
            """
            카운트를 하나 증가시킴

            :return:
            """
            self.count += 1

    def get(self):
            """
            count 값을 반환

            :return:
            """
            return self.count
#실행 코드 시작
# class counter의 instance를 생성해서 변수 a에 저장
a = Counter() #counter는 클래스 이름. ()가 있어야 한다. __init__(self)가 호출됨 클래스가 디폴트값으로 저장
#class Counter의 instance를 생성해서 변수 b에 저장
b = Counter(10)
#a.reset()
#변수에 .을 이용하여 메소드 호출. self 매개변수값이 되어 넘어감
a.increment()
a.increment()
a.increment()
print("a=%d" %a.get())

#b.reset()
print("b=%d" %b.get())