sample_list=["hello","world","of","program"]
text_file=open("sample_list.txt","w")
for element in sample_list:
    text_file.write(element+"\n")
text_file.close