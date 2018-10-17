x = input()
def sum_digit(x):
    sum=0
    for i in range(0,len(x)):
        sum+=int(x[i])
    return sum

print(sum_digit(x))
