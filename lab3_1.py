"""
쳅터: day3 데이터형 연습
주제: 데이터형 연습
작성자: 윤경환
작성일: 18.09 04

"""

f = 3.4 #f의 데이터타입은 float 왜냐하면, 3.4가 실수이기 떄문이다
print(f)
i = 3 #i의 데이터타입은 int. 왜냐하면, i에 정수인 3이 저장되었으므로
print(i)
b = True #b는 boolean type. 왜냐하면, b에 true가 저장되었으므로.(boolean type은 true 또는 false를 저장한다
print(b)
s="안녕하세요" #s는 문자열 str 문자열은 " "로 묶는다. 또는 ''로 묶는다.
print(s)
s='1' #s의 데이터 타입은 str
print(s)

#f와 i를 더해서 출력, i가 float로 자동 변환되어 계산됨
print(f+i)

#s+i 더해서 출력
#오류발생 왜냐하면, 문자열이 int로 자동변환되지는 않는다.
#print(s+i)

#s를 int로 형 변환하여 i와 더하기
print(int(s)+i)

#i를 str로 형변환하여 s와 더하기. 문자열 이어주기 연산이 실행됨
print(s+str(i))

#정수 계산
print("정수 나누기")
i=57
j=28

#i를 j로 나눈 값 출력
print(i/j)

#i를 j로 나눈 몫 출력
print(i//j)

#i를 j로 나누었을 때 나머지 출력
print(i%j)

#j의 제곱 출력
print(j**2)

#j의 세제곱 출력
print(j**3)

#실수 계산
print("실수 나누기")
i=57.0
j=28.0

#i를 j로 나눈 값 출력
print(i/j)

#i를 j로 나눈 몫 출력
print(i//j)

#i를 j로 나누었을 때 나머지 출력
print(i%j)

#j의 제곱 출력
print(j**2)

#j의 세제곱 출력
print(j**3)

print(100000000000000000000000)

# or 연산자(boolean type 연산자)
print(b or False)

# and 연산자(boolean type 연산자)
print(b and False)
print(True and b)
print(False and False)

#복소수(실수부와 허수부ㅜ로 구성된 숫자)타입 변수 k
k = 5 + 7j
print(k)
print(k.real) #복소수의 실수부를 출력
print(k.imag) #복소수의 허수부를 출력

print(k.conjugate()) #켤레 복소수를 가져오는 함수 호출

# 8진수 표현

o = 0o16 #십진수로는 14를 의미, 실제 테이터 타입은 int
print(o) #기본 십진수
print("%o" %o) #8진수로 출력됨
print("%x" %o)#16진수로 출력됨. %x는 소문자로 출력, %X는 대문자로 출력

#16진수 표현

x=0xA5
#십진수 출력
print(x)
#8진수 출력
print("%o" %x)
#16진수 출력
print("%x" %x)