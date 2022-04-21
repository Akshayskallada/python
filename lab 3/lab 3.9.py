from cgitb import text
from itertools import count


f =open("hello.txt","r")
count=0
text =f.read()
list =text.split("")
for x in list:
    if x:
        count =count+1
print("Total number of lines in the text file is:",count)

