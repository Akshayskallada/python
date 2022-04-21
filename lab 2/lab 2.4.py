Char = 0
CharList = []
k = 0
print("Enter the String: ")
text = str(input())
textList = list(text)
total = len(text)
for i in range(total):
  if text[i] in textList:
    if text[i] not in CharList:
      newText = text[i+1:]
      newTotal = len(newText)
      for j in range(newTotal):
        if newText[j]==text[i]:
          Char = Char+1
          CharList.insert(k, text[i])
          k = k+1
          break
print("Total Repeated Characters is : ")
print(Char)