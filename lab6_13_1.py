"""
 쳅터: day6
 주제: exception
 문제: 사용자로부터 숫자를 입력받아, 1부터 해당숫자까지의 합을 구하라
 만약 숫자가 아닌 값이 입력되면, "숫자를 입력하세요" 라는 문장을 출력한 후 다시 입력을 받는다.
 작성자: 윤경환
 작성일: 18 11 27
"""
# exception을 사용하여 프로그래밍
sum = 0
while True:
    try:
        x = int(input()) #int로 변환되는 과정에서 ValueError 발생 시 except에 반환됨
        for i in range(1,x+1):
            sum += i
        break
    except ValueError:
        print("숫자를 입력하시오")
print(x,"까지의 합:",sum)