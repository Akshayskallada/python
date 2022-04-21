def sub_list (l):
    list = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            list.append(l[j: i])
    return list
l1 = [1, 2, 3]
print(sub_list(l1))