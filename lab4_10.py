"""
쳅터: day 4
주제: 반복문
작성일: 18.09.27
문제: 사용자가 입력한 영문자를 아래와 같이 출력
(예)
BINGO
 INGO
  NGO
   GO
    O

작성자: 윤경환
"""

s = input()

for i in range(0,int(len(s))):

    for k in range(0,int(len(s))):
        if (i==k):
            for a in range(0,k):
                print(" ",end="")


    print(s[i:],end="")
    print("")

