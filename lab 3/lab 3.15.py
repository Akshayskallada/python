import random
f=open("hello.txt","r")
data=f.readlines()
print("random line:",random.choice(data))