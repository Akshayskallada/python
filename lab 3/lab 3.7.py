content_array=[]
with open("hello.txt") as f:
    for line in f:
        content_array.append(line)
    print(content_array)
    
