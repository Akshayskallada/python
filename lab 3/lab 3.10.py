dic = {}
with open("hello.txt" ,'r') as f:
    for line in f:
        l1 = line.split(" ")
        for w in l1:
            dic[w] = dic.get(w,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))