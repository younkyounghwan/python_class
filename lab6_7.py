"""
 chapter: day6
 subject: regular expression
 problem: re ..?*+ sign practice
 writer: 윤경환
 date: 18 11 15
"""
import re #regular expression

# define each string case with test
s = "teeeest"
s2 = "tetst"
s3 = "tst"

r = re.compile("e.s") # find case that exist between e and s
print(r.search(s))
print(r.search(s2))
print(r.search(s3))
print("======================================")

r = re.compile("e?s") # after e appears 0-1 time, find case that appears s
print(r.search(s))
print(r.search(s2))
print(r.search(s3))
print("======================================")

r = re.compile("e*s") #after e exist more than 0 time, find case appears s
print(r.search(s))
print(r.search(s2))
print(r.search(s3))
print("======================================")

r = re.compile("e+s") #after e exist more than 1 time, find case appears s
print(r.search(s))
print(r.search(s2))
print(r.search(s3))