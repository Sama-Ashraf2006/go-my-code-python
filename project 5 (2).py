#!/usr/bin/env python
# coding: utf-8

# In[54]:


#question 1
class point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def name(self):
        return(self.x,self.y,self.z)
        self.x=x
        self.y=y
        self.z=z
k = point3D(2,8,5)
k.name()

        


# In[40]:


#question 2
class rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return(self.x*self.y)
    def perimeter(self):
        return((self.x+self.y)*2)
rec1 = rectangle(10 , 12)
print(rec1 . area())
print(rec1 . perimeter())


# In[45]:


#question 3
class circle:
    def __init__(self , center , radius):
        self.center= center
        self.radius= radius
    def area(self):
        return(3.14* self.radius)
    def perimeter(self):
        return(2*3.14*self.radius)
c1 = circle(0,4)
print(c1. area())
print(c1. perimeter())


# In[4]:


#question 4
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()


# In[ ]:




