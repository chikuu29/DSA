# Input: text = gotxxotgxdogt, word = got
# Output : 3

def result(text,word):
    length=len(word)
    count=0
    start=0
    windowArray=''
    for end in range(len(text)):
        # print("A")
        if end-start+1==length:
        #  print("x",length)
         tcount=0
         for i in word:
            # print('l',i)
            # print(text[start:end+1])

            if i in text[start:end+1]:
                # print(i)
                tcount+=1
         if tcount==length:
            count+=1
         start+=1       
        windowArray+=text[end]

    return count




text="oattog";
word="got"
print(result(text,word))