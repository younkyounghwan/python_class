"""
 chapter: day6
 subject: regular expression
 problem: re sign practice
 writer: 윤경환
 date: 18 11 15
"""
import re #regular expression

# define each string with test
s = "teeeest"
s2 = "tetst"
s3 = "tst"
s4 = "apple"
s5 = "test1234"

r = re.compile("\d") # return after finding number
print(r.search(s))
print(r.search(s5))
print("======================================")

r = re.compile("\D") # return after finding non number
print(r.search(s))
print(r.search(s5))
print("======================================")

r = re.compile("[a-zA-Z]") # return after finding alphabet
print(r.search(s))
print(r.search(s5))
print("======================================")