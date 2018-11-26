x = input() #입력
def ceil(x): # 올림
    if float(x) == float(x)//1:
        print(int(float(x)))
    else:
        print(int(float(x)//1 + 1)) #계산

def floor(x): # 내림
    if float(x) == float(x)//1:
        print(int(float(x)))
    else:
        print(int(float(x)//1)) #계산

def round(x): # 반올림
    if (float(x) - int(float(x)//1)) >= 0.5:
        print(int(float(x) // 1 + 1))
    else:
        print(int(float(x) // 1))

ceil(x) #호출
floor(x)
round(x)