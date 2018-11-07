"""
201814099 윤경환
"""
def cul(a,b): #약분
    if (a>=b):
        while b!=0:
            c=a%b
            a=b
            b=c
        return a
    else:
        while a!=0:
            c=b%a
            b=a
            a=c
        return b

class Fraction: #class 정의
    def __init__(self,n,d):
        self.denom = d #분모
        self.numer = n #분자
    def __str__(self):
        if self.denom<0 and self.numer>0:
            s = "("
            s = s + str(-self.numer) + "/" + str(-self.denom) + ")"
        else:
            s = "("
            s = s+str(self.numer)+"/"+str(self.denom)+")"
        return "{}".format(s)
    def plus(self, o):
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.denom + o.numer * self.denom
        r = Fraction(n//cul(n,d), d//cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def diff(self ,o):
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.denom - o.numer * self.denom
        if d<0:
            d = -d
        r = Fraction(n//cul(n,d), d//cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return  r

    def mul(self,o):
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.numer
        r = Fraction(n//cul(n,d), d//cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def div(self,o):
        # 결과의 분모 계산
        d = self.denom * o.numer
        # 결과의 분자 계산
        n = self.numer * o.denom
        r = Fraction(n//cul(n,d), d//cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return r
    def equal(self,o): #같을 때
        n =  self.numer / self.denom #비교하기 위한 밑작업
        d =  o.numer / o.denom
        if n==d: #조건
            return True
        else:
            return False

    def differ(self,o): #다를 때
        n = self.numer / self.denom
        d = o.numer / o.denom
        if n != d:
            return True
        else:
            return False

    def ris(self,o): # <
         n = self.numer / self.denom
         d = o.numer / o.denom
         if n-d < 0:
             return True
         else:
             return False

    def rise(self,o): # <=
         n = self.numer / self.denom
         d = o.numer / o.denom
         if n-d <= 0:
             return True
         else:
             return False

    def lis(self, o): # >
        n = self.numer / self.denom
        d = o.numer / o.denom
        if n-d > 0:
            return True
        else:
            return False

    def lise(self,o): # >=
        n = self.numer / self.denom
        d = o.numer / o.denom
        if n-d >= 0:
            return True
        else:
            return False

s1 = Fraction(-4,5) #분자 분모 입력
s2 = Fraction(3,2)
print(s1,end=" * ") #출력
print(s2,end=" = ")
print(s1.mul(s2))

s1 = Fraction(8,31) #분자 분모 입력
s2 = Fraction(2,3)
print(s1,end=" - ") #출력
print(s2,end=" = ")
print(s1.diff(s2))

s1 = Fraction(3,5) #분자 분모 입력
s2 = Fraction(3,7)
print(s1,end=" + ") #출력
print(s2,end=" = ")
print(s1.plus(s2))

s1 = Fraction(4,8) #분자 분모 입력
s2 = Fraction(1,2)
print(s1.equal(s2)) #출력

s1 = Fraction(2,81) #분자 분모 입력
s2 = Fraction(3,9)
print(s1.lise(s2)) #출력