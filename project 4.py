#!/usr/bin/env python
# coding: utf-8

# In[9]:


#question 1
x=19
y=80
z=15
max_v=max(x,y,z)
print(max_v)
    


# In[2]:


#question 1
x=[20,19,35]
max_v=max(x)
max_v


# In[4]:


#question 2
result = lambda x,y : (x+y,x-y)
result(300,70)


# In[33]:


#question 3
l1=[1,2,5,7]
x = 0
y=len(l1)  #(4)
for i in (l1):
    print(i+y)


# In[45]:


#question 3
l1=[1,2,5,7]
x = 0
y=len(l1)
for i in (l1):
    print(i*y)


# In[43]:


x=[1,2,6,5,8,7,10]
for i in (x):
    if i%2==0:
        print(i*i)


# In[46]:


tuple1=(1,2,3)
tuple2=(5,1,7)
result=list(map(lambda x,y : x+y ,tuple1 , tuple2))
result


# In[3]:


#question 3
l1=[1,2,5,7,4,6]
x = 0
y=len(l1)  #(4)
for i in (l1):
    if  i%2== 0:
        u=0
        print(i+u)


        
    
   
   


# In[14]:


#question 4
def my_dict(s):
    for i in s:
        print(s[i].title())
s={"dada":"sasa" , "fafa":"haha", "gaga":"yaya" , "tata":"papa" , "oaoa":"iaia" , "wawa":"qaqa" , "kaka":"mama" , "nana":"vava" , "caca":"xaxa" , "zaza":"uaua" }
my_dict(s)


# In[19]:


#question 5
def my_dict(q):
    x=len(q)
    y=[q]
    for i in q:
        if (len(i) > x):
            x=len(i)
            y=i 
    print("the word is:", y ,"and the length is", x)
q={"lion":"bees" ,"animal":"tigar","giraff":"cat","monkey":"dog"}     
my_dict(q)  
       
        
        
        


# In[61]:


#question 6
my_string=input("enter a string : ")
my_string=my_string.split("-")
my_string.sort()
print(my_string)


# In[10]:





# In[ ]:





# In[ ]:




