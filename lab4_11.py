"""
쳅터: day 4
주제: 반복문(for문)
문제: 사용자로부터 5개의 숫자를 입력받아, 이를 리스트에 저장한후 합과 평균을 구하여 출력한다.
작성자:윤경환
작성일: 18 09 20
"""

s=input()
l=[]
sum=0
for j in range(0,5):
    l.append(s[j])
for i in range(0,5):
    l.insert(i,int(l[i]))
for n in  range(0,5):
    sum+=l[n]

print("합:%d"%(sum))
print("평균:%d"%(int(sum)/5))




