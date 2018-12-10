"""
챕터: day7
주제: file 쓰기
문제:
현재 디렉토리 아래에 fruit.txt 파일을 생성하여, 사용자가 입력하는 과일을 한 줄에 하나씩 3개를 저장하라.
작성자: 윤경환
작성일: 2018.12.06
"""
import os.path
print(os.getcwd())
f = open("friut.txt","wt") # at, wt
x = input("과일: ") # 과일이름
x1 = int(input("가격: ")) # 과일가격
y = input("과일: ")
y1 = int(input("가격: "))
z = input("과일: ")
z1 = int(input("가격: "))
f.write(x+" - ")
f.write(str(x1)+"\n")
f.write(y+" - ")
f.write(str(y1)+"\n")
f.write(z+" - ")
f.write(str(z1)+"\n")
f.close()