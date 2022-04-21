from re import A


a = eval(input("Enter first list :-"))
b = eval(input("Enter second list :-"))
list = [ ] 

for i in a :
      if i in b :
            list.append( i )

for i in list :
      if list.count( i ) > 1 :
            list.remove( i )

print("Comman elements are :-", list)
