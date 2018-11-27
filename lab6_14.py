"""
 쳅터: day6
 주제: exception
 문제: 사용자로부터 두 수를 입력 받아, 첫번쨰 수를 두번째 수로 나눈 값을 출력한다.
 두번째 수가 0이 입력되는 경우(ZeroDivisionError), "0으로 나눌 수 없습니다."라는 문장을 출력한 후 다시 두 수를 입력받아 계산한다.
 작성자: 윤경환
 작성일: 18 11 27
"""
x = int(input())
while True:
    try:
        y = int(input())
        print(x / y)
        break
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except ValueError:
        print("숫자를 입력하시오")