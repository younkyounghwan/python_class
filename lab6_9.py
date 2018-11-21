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
s5 = "test1234Test"
s6 = "나는 \"왕\"이다"

r = re.compile("\d") # return after finding number
print(r.search(s)) # recall the compile that define with re which means module
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

# using search that function, rewrite code that line 25-27
print(re.search("[a-zA-Z]",s))
print(re.search("[a-zA-Z]",s5))

#search alphbet or number in s5
print(re.search("[a-zA-Z0-9]",s5))


#search number in s5
print(re.search("[0-9]",s5))

#search captial alphbet in s5
print(re.search("[A-Z]",s5))

#search lower alphbet in s5
print(re.search("[a-z]",s5))

#search location of \ in s6
print(re.search("[\\\]",s6))