m = int(input("m:"))
n = int(input("n:"))
sum = 0
l=[]
a = 0
while(1):
    a+=1
    b=a**2
    if(b>n):
        l.append(b)
        break
    if(b>=m):
        sum+=b
        l.append(b)

print(sum)
print(l[0])