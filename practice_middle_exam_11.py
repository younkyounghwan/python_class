s = input()
print(s)
s = sorted(set(s))
for i in s:
    print(i,end="")