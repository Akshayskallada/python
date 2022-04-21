n=int(input("how many numbers you want in list:"))
list1=[]
for i in range(n):
    list1.append(int(input()))
sum_list1=0
for i in list1:
    sum_list1=sum_list1 + i
print("sum of list is :",sum_list1)           