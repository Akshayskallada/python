f = open("hello.txt","r")
str = f.read()
words = str.split()
max_len = len(max(words, key=len))
for word in words:
    if len(word)==max_len:
        longest_word =word
         
print(longest_word)