#!/usr/bin/env python
# coding: utf-8

# In[7]:


#question 1
import requests
from bs4 import BeautifulSoup
import csv
link = "https://en.wikipedia.org/wiki/History_of_Japan"
req = requests.get(link)
soup = BeautifulSoup(req.content , "html.parser")
print(soup.prettify())


# In[10]:


#question 2
print ("the title of this page is :" )
for title in soup.find_all('title'):
    print(title.get_text())


# In[25]:


#question 3
import requests
from bs4 import BeautifulSoup
link = "https://en.wikipedia.org/wiki/History_of_Japan"
req = requests.get(link)
soup = BeautifulSoup(req.content , "html.parser")
print(soup.find_all('h2')[1])
print(soup.find_all('p'))
print(soup.get_text())


# In[31]:


#question 4
links = [a["href"] for a in soup.find_all("a", href=True)]
print(links)


# In[57]:


#question 5
import requests
from bs4 import BeautifulSoup
def gut(link):
    req = requests.get(link)
    soup = BeautifulSoup(req.content , "html.parser")
    print(soup.prettify())
    print ("the title of this page is :" )
    for title in soup.find_all('title'):
        print(title.get_text())
    print(soup.find_all('h2')[1])
    print(soup.find_all('p'))
    print(soup.get_text())
    links = [a["href"] for a in soup.find_all("a", href=True)]
gut("https://en.wikipedia.org/wiki/History_of_Japan")


# In[ ]:





# In[ ]:




