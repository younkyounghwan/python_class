"""
챕터: day7
주제: file 읽기
문제:
friut.txt 파일에 저장되어 있는 과일 이름들을 출력하라. 몇줄의 과일이 저장되었든지 상관없이 출력됨을 보장하라.
내가 산 과일 가격의 합을 출력하라.
작성자: 윤경환
작성일: 2018.12.06
"""
import os.path
f = open("friut.txt","rt")
l = f.readlines()
sum = 0
for s in l:
    fr = s.split("-")
    print("과일명: ", fr[0])
    print("과일가격: ", fr[1])
    sum +=int(fr[1])
print("과일가격 합:",sum)