with open("hello.txt") as f:
    with open ("sample.txt","w") as f1 :
        for line in f:
            f1.write(line)