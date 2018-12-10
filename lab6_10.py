"""
 chapter: day6
 subject: regular expression
 problem: practice re sign
 writer: 윤경환
 date: 18 11 15
"""
import re
s5 = "Test1234Test"
s7 = 'href =      "C:\Python34\kim.jpg"'
s8 = 'href ="C:\Python34\Kim.jpg"'
# search where space appears in s7
print(re.search("\s",s7))

# search first time where white space doesn't appears in s7
print(re.search("\S",s7))

print("0===================")
#search where 'href =' is in s7 and s8.
#because of searching one pattern in each string, use search after compile
r = re.compile("href =")
print(r.search(s7))
print(r.search(s8))

print("1===================")

# search where 'href =' is in s7, not consider space surrounding =
r = re.compile("href\s*=\s*")
print(r.search(s7))
print(r.search(s8))

print("2===================")

#using group
r = re.compile("href\s*=\s*\"")
result = r.search(s7)
print(result.group()) #return matched group

print("3===================")

# split by =
print(re.split("=",s8))

# change string to other string
print(re.sub("e+","i",s7))

# return all matched string by list
print(re.findall("\d",s5)) #[1,2,3,4]

print("4===================")

#split two subgroup not consider surrounded = space in s7
r= re.compile("(href\s*=\s*)(\".*\")") #to split subgroup use ()
result = r.search(s8)
print(result.group(0)) # 0 is all matched. default is 0
print(result.group(1)) # 1 is part matched first ()
print(result.group(2)) # 2 is part matched second ()
print(result.groups()) # return subgroup by tuple