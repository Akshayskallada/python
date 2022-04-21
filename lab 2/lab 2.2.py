n=input("Enter any string:")
ch = input("Enter search character ")
f = 0
for i in n:
    if i==ch:
        f=f+1
print("Number of time found =",f)