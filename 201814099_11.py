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


class Fraction:
    def __init__(self,n,d):
        """

        :param a:
        :param b:
        """
        self.denom=d
        self.numer=n

    def plus(self, o):
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.denom + o.numer * self.denom
        r = Fraction(n/cul(n,d), d/cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def diff(self ,o):
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.denom - o.numer * self.denom
        if n<0:
            n = -n
        r = Fraction(n/cul(n,d), d/cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return  r

    def mul(self,o):
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.numer
        r = Fraction(n/cul(n,d), d/cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def div(self,o):
        # 결과의 분모 계산
        d = self.denom * o.numer
        # 결과의 분자 계산
        n = self.numer * o.denom
        r = Fraction(n/cul(n,d), d/cul(n,d))  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def setNumer(self,n):
        self.numer = n

    def setNenom(self,d):
        self.denom = d


        # 분자를 반환하는 메쏘드 get_Numer 정의

    def getNumer(self):
        return self.numer

        # 분모를 반환하는 메쏘드 get_denom 정의

    def getDenom(self):
        return self.denom

    def print(self):
        print("%d/%d" %(self.numer, self.denom))


bunsu1 = Fraction(1,2)
bunsu2 = Fraction(5,4)

bunsu1.print() #plus
print("+")
bunsu2.print()
print("=")
bunsu1.plus(bunsu2).print()
print("")

bunsu1.print() #diff
print("-")
bunsu2.print()
print("=")
bunsu1.diff(bunsu2).print()
print("")

bunsu1.print() #mul
print("*")
bunsu2.print()
print("=")
bunsu1.mul(bunsu2).print()
print("")

bunsu1.print() #div
print("/")
bunsu2.print()
print("=")
bunsu1.div(bunsu2).print()
print("")

