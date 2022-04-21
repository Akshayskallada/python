import os
filepath="hello.txt"
size=os.path.getsize(filepath)
print(str(size) + ' Bytes')