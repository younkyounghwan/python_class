d = input().split() #입력
for i in range(0,3): #형변환
    d[i] = int(d[i])
a = max(d) #최대값
def cul(): #최대값을 리스트에서 제거
    b =  d.index(a)
    del d[b]
    return d
cul()
if (a>sum(d)): #조건
    print("삼각형이 성립될 수 없습니다.")
elif (a**2==d[0]**2+d[1]**2): #조건
    print("직각삼각형입니다.")
else: #조건
    print("삼각형입니다.")