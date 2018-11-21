"""
 chapter: day6
 subject: regular expression
 problem: practice re sign
 writer: 윤경환
 date: 18 11 15
"""
import re
s7 = 'href =      "C:\Python34\kim.jpg"'
s8 = 'href ="C:\Python34\kim.jpg"'
# search where space appears in s7
print(re.search("\s",s7))

# search first time where space doesn't appears in s7
print(re.search("\S",s7))
#search where 'href=' is in s7 and s8.
#because of searching one pattern in each string, use search after compile
r = re.compile('href=')
print(r.search(s7))
print(r.search(s8))

# search where 'href=' is in s7, not consider space surrounding =

r = re.compile("href\s*=\s*")
print(r.search(s7))
print(r.search(s8))

