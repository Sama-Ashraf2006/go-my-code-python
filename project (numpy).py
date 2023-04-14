#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np 
x=int(input("num of student "))
y=int(input("num of subj "))
k=np.array([])
for i in range (x):
    temparray=np.array([])
    for j in range(y):
        temp=int(input("num of marks "))
        temparray = np.append(temparray,temp)
    print(temparray)
    k = np.concatenate((k,temparray))
k = k.reshape(x,y)
print(k)
o=np.sum(k,axis=1)
print(o)
if j >=90:
    print("A+")
elif j >=80:
    print("A")
elif j >=70:
    print("B+")
elif j >= 60:
    print("B")
elif j>= 50:
    print("c")
else:
    print("fail")

