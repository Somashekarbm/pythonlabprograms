#lab program 3(B)
str1=input()
str2=input()
if len(str2)<len(str1):
    short=len(str2)
    long=len(str1)
else:
    short=len(str2)
    long=len(str2)
matchcnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchcnt+=1
print("similarity between two said strings")
print(matchcnt/long)
