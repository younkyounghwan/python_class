"""
 chapter: day6
 subject: regular expression
 problem: re ^$[^][-]sign practice
 writer: 윤경환
 date: 18 11 15
"""

import re #regular expression

# define each string with test
s = "teeeest"
s2 = "tetst"
s3 = "tst"

print("1 ======================================")
r = re.compile("^t") # return part started "t" after find
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

print("2 ======================================")
r = re.compile("t$") # return part finished "t" after find
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

print("3 ======================================")
r = re.compile("[^te]") # find case of not "te"
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

print("4 ======================================")
r = re.compile("[a-m]") # find a to m
print(r.search(s))
print(r.search(s2))
print(r.search(s3))

