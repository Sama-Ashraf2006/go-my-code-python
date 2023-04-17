#!/usr/bin/env python
# coding: utf-8

# In[14]:


#question 1
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] }

df = pd.DataFrame (exam_data)
dh = df.head(3)
dh


# In[17]:


#question 2
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df = pd.DataFrame(exam_data , columns = ["score"])
df = df.dropna()
df= df.reset_index(drop = True)
df


# In[26]:


#question 3
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df = pd.DataFrame (exam_data)
select = df[["name" , "score"]]
print(select)


# In[50]:


#question 4
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df = pd.DataFrame(exam_data)
display(df)
df2 = {"name": "Suresh", "score": 15.5, "attempts": 1, "qualify": "yes", "labels": "s"}
df = df.append(df2, ignore_index = True)
display(df)


# In[39]:


#question 5
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df = pd.DataFrame(exam_data)
del df["attempts"]
df


# In[58]:


#question 6        
#first method
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df = pd.DataFrame(exam_data)
df["success"] = ["1" if x > 10 else "0" for x in df["score"]]
df


# In[62]:


#question 6
#second method
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df = pd.DataFrame(exam_data)
df["success"] = np.where (df["score"] > 10 ,"1" , "0")
df


# In[65]:


#question 7
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],

'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}

df = pd.DataFrame(exam_data)
print('DataFrame:\n', df)
gfg_csv_data = df.to_csv('GfG.csv', index = True)
print('\nCSV String:\n', gfg_csv_data)


# In[ ]:




