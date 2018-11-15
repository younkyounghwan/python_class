"""
 chapter: day6
 subject: 정규식 regular expression
 problem: compile. match, search standard practice
 writer: 윤경환
 date: 18 11 15
"""
import re #regular expression module import
r = re.compile("p.") #recall the compile of re module. wanna find "p". when you find particular string, use regluar
                    # return expression object. . means unexpected string
print(r.search("pizza")) # r.search return "p." in "pizza" of string imformation matched particular part
print(r.match("pizza")) # r.match return first "p." in "pizza" of string imformation matched particular part

r = re.compile("[z]") #recall the compile of re module. wanna find one if the "a, e, i ,o ,u". when you find particular string, use regluar
                    # return expression object. write the string you wanna find in []
print(r.search("pizza")) # r.search return [z] in "pizza" of string imformation matched particular part
print(r.match("pizza",2)) # r.match return first [z] in "pizza" of string imformation matched particular part

