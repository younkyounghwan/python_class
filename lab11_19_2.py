x = int(input()) #항 입력
a = 0 # 앞 변수
b = 1 # 뒷 변수
print(a) # 첫항
for i in range(1,x): # 반복문
    print(b) # 출력
    c = a # 계산
    a = b
    b += c