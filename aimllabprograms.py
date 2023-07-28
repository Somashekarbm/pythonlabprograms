#!/usr/bin/env python
# coding: utf-8

# In[3]:


print('my name is')
for i in range(5):
    print('Jimmy Five Times('+str(i)+')')
    


# In[4]:


val=str(input("enter a value:"))
str_val=str(val)
if str_val==str_val[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i),"appears",str_val.count(str(i)),"times")


# In[1]:


def fn(n):
    if n==1:
        return 0;
    elif n==2:
        return 1
    else:
        return fn(n-1)+fn(n-2)
    
num=int(input("enter a number:"))
if num>0:
    print("fn(",num,")=",fn(num),sep="")
else:
    print("error in input")
    


# In[5]:


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


# In[5]:


def bin2Dec(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*2**i
        i+=1
    return dec
def oct2hex(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig) * 8**i
        i+=1
    list=[]
    while dec!=0:
        list.append(dec%16)
        dec=dec//16
        nl=[]
        for elem in list[::-1]:
            if elem<=9:
                nl.append(str(elem))
            else:
                nl.append(chr(ord('A')+(elem-10)))
        hex="".join(nl)
    return hex
num1=input("enter a binary number:")
print(bin2Dec(num1))
num2=input("enter a octal number:")
print(oct2hex(num2))
    
        


# In[ ]:


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


# In[8]:


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
        


# In[9]:


var="fstring"
print(f"this is a variable allocation using f string {var}")


# In[19]:


list=[10,20,30,40]
list.index(40)
list.append(50)
print(list)
list.remove(50)
print(list)
list.insert(0,5)
print(list)
list.remove(5)
print(list)
list.pop(0)
print(list)


# In[25]:


list=['shreyas','prank','special','nigga']
print(len(list))
if key in list:
    print("shreyas is found")
print(list[4])


# In[32]:


list1=[["cat","bat"],[10,20,30]]
print(list1[1][2])
if list1[0][0]==list1[-2][0]:
    print(True)


words=["hello","hi","abcd","yello"]
words[1:]
words[:-1]


# In[47]:


list3=[[10,20,30],['hello','how','boy'],[10.2,10,20]]
print(list3[0][1])
print(list3[1][0])
print(list3[2][0])
list=['cat','bat','elephant']
list[2]='rat'
list3*5
del list3[2]
print(list3)


# In[ ]:





# In[ ]:





# In[ ]:


catnames=[]
while len(catnames)>=0:   #or while True
    print('enter the name of cat '+str(len(catnames)+1)+'(or enter nothing to stop)')
    name=input()
    if name=="":
        break
    catnames=catnames+[name]
print('the cat names are:')
for name in catnames:
    print(' '+name)


# In[1]:


for i in range(20):
    print(i)


# In[1]:


for i in 1,2,3,4:
    print(i)


# In[2]:


'howdy' in [10,20,'howdy']


# In[4]:


#use of in and not in operators
pet_names=['raju','chutki','sisya','baro']

name=input('enter a pet name')
    
if name in pet_names:
    print(f"{name} is my pet")
else:
    print(f"i dont have a pet named {name}")
      


# In[7]:


cat=['fat','gray','loud']
size,color,disposition=cat
print(size,color,disposition)


# In[10]:


#enumerte() function gives index,item of the list
supplies=['pens','staplers','flamethrowers','binders']
for index,item in enumerate(supplies):    #gives like tuples of (index.item(at index))
    print("index: "+str(index)+' in supplies is :'+item)


# In[25]:


#random library
import random
pets=['dog','cat','bat']
print(random.choice(pets))
random.shuffle(pets)
pets


# In[48]:


#comprehension in python
list=['shreyas','soma','roops','naveen']
new_list=[ ('hello',x) for x in list if x!='naveen']
print(new_list)


# In[ ]:





# In[ ]:




