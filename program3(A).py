#program 3(A)
sentence=input("enter a sentence:")
wordList=sentence.split(" ")
print("this sentence has",len(wordList),"words")
digcnt=upcnt=locnt=0
for ch in sentence:
    if '0'<=ch<='9':
        digcnt+=1
    elif 'A'<=ch<='Z':
        upcnt+=1
    elif 'a'<=ch<='z':
        locnt+=1
print("this sentence has:",digcnt,"digits",upcnt,"upper case letters",locnt,"lower case letters")
