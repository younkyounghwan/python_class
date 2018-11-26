"""
 chapter: day6
 subject: 정규식 regular expression
 problem: compile. match, search standard practice
 writer: 윤경환
 date: 18 11 15
"""
import re # import regular expression module
r = re.compile("p.") # recall the compile of re module. if wanna find "p". when you find particular string, use regular
                     # return expression object. it means unexpected string
print(r.search("pizza")) # r.search return "p."  of string information matched particular part in "pizza"
print(r.match("pizza")) # r.match return first "p." of string information matched particular part in "pizza"

r = re.compile("[z]") #  recall the compile of re module. wanna find one if the "a, e, i ,o ,u". when you find particular string, use regluar
                      # return expression object. write the string you wanna find in []
print(r.search("pizza")) # r.search return [z] in "pizza" of string imformation matched particular part
print(r.match("pizza",2)) # r.match return first [z] in "pizza" of string imformation matched particular part

