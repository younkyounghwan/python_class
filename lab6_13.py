"""
 쳅터: day6
 주제: exception
 문제: 사용자로부터 숫자를 입력받아, 1부터 해당숫자까지의 합을 구하라
 만약 숫자가 아닌 값이 입력되면, "숫자를 입력하세요" 라는 문장을 출력한 후 다시 입력을 받는다.
 작성자: 윤경환
 작성일: 18 11 27
"""
# exception을 사용하지 않고 프로그래밍
import re
sum = 0
while True:
    x = input()
    r = re.compile("^[0-9]+$")
    if r.search(x) == None:
        print("숫자가 아닙니다.")
        continue
    for j in range(1,int(x)+1):
        sum += j
    break
print(x,"까지의 합:",sum)