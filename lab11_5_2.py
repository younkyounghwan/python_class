x, y = input().split() #키 몸무게 입력
x = int(x) #형변환
y = int(y)
x = x/100 #미터로 바꿈
z = y/(x**2) #bmi 계산
if (z<15): #조건
    print("저체중")
elif (z<20):
    print("정상")
elif (z<30):
    print("경도비만")

else:
    print("고도비만")
