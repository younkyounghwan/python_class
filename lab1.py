number="hi"
print(number)
number=10
print(number)


a=5
b=25
c=a+b
# 5+25=30을 출력하라
msg="%d+%d=%d" #출력하고자하는 문자열도 변수로 정의할 수 있다.
print(msg%(a,b,c))
print("%d+%d=%d"%(a,b,c)) # 서식문자를 여러개 이용할 경우 괄호 안에 넣기

#문자열 출력
money=10000
print("나는 현재%d원이 있습니다."%money) #서식문자를 이용할 수 있다.컴마없이 변수이름 앞에 %를 쓴다.

#입력
money = input("얼마를 가지고 게세요?")
print("입력하신 값은 %s원입니다."%money) #%s로 받음