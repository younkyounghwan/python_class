"""
 chapter: day6
 subject: regular expression
 problem: practice re sign
 writer: 윤경환
 date: 18 11 22
"""
import re
"""
1. compile a in apple
2. compile b in apple
3. 정규식을 이용하여, 사용자가 입력한 영어 문장에서 a,e,i,o,u가 포함되어 있는지 찾아서 출력하시오. 만족하는 첫번째 만 출력한다.
<입력> This is a test
"""
s1 = "apple"
r = re.compile(s1)

"""
4. 입력한 단어가 a로 시작하는 지 확인
5. 입력한 단어가 e로 끝나는 지 검사
"""

"""
7. 입력된 문장에서 숫자부분을 모두 출력하라.
A. 입력 예: 2017년 3월 8일 5000원
B. 출력 예:
2017
3
8
5000

"""
s = "2017년 3월 8일 5000원"
r = re.compile("\d")
result = r.search(s)
print(result.findall())

"""
10. 입력된 문장에서 <이후에 나오는 단어들을 출력하라.
A. 입력 예: <2015> <김일수> <성공회대학교>
"""
