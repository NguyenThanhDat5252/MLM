#!/usr/bin/env python
# coding: utf-8

# # getting and knowing data

# import pandas as pd 
# import numpy as np
# 

# In[2]:


import pandas as pd
import numpy as np


# reading data
# 

# In[3]:


df = pd.read_csv("chipotle.tsv", sep = "\t")


# In[4]:


df.head(5)


# dataset overview
# 

# In[5]:


df.shape
# 4622 rows , 5 columns


# In[6]:


df.info() # return info of colums


# In[9]:


# print all columns's name
print(df.columns)
list(df.columns)


# In[10]:


df.index


# In[13]:


df.describe() # return thông tin những columns chỉ chứa số  (thống kê)


# In[14]:


df.describe(include = "all")


# ##loc vs iloc = location and index location
# 

# In[21]:


df.head()


# In[30]:


df.loc[(df.quantity == 15) | (df.item_name == "Nantucket Nectar")] # we use | not use "or"


# In[31]:


df.loc[(df.quantity == 2) & (df.item_name == "Nantucket Nectar")] # use & not use "and"


# In[33]:


df.loc[(df.quantity == 15) | (df.item_name == "Nantucket Nectar"),['order_id','quantity',"item_name"]] # only return 3 columns 
"order_id", "quantily","item_name" 


# In[36]:


#iloc : index location
df.iloc[[9]] # return the 9th rows start with 0


# In[40]:


df.iloc[3:11] # row start = 3 row end = 11 


# In[42]:


df.iloc[3:7, 0:-1] # columns start = 0 columns end = -1 and don't take column -1


# In[43]:


df.iloc[3:7,2] # only take column 2 index start with 0


# Data Manipulation

# In[44]:


df.item_price.dtype


# In[47]:


# convert dtype of item_price to float
df.item_price.apply(lambda x : float(x.replace("$",''))) # chỉ thay đổi nhất thời 


# df.item_price.dtype

# In[48]:


df.head()


# In[49]:


# rewrite
df.item_price = df.item_price.apply(lambda x : float(x.replace("$",'')))
df.head()
# it remove $ and the element of item_price column is float


# In[53]:


# add one or more columns
df["total_price"] = df.quantity * df.item_price # or df['total_price'] = df['quantity'] * df["item_price"]
df.head() # have one new column


# In[54]:


# tổng doanh thu = tổng total_price = revenue
df["total_price"].sum()


# In[63]:


# which was the most - odered item ?
# use group by
c = df.groupby("item_name")["quantity"].sum()
print(c)


# In[65]:


# sort_values
c.sort_values().head(5) # tăng dần


# In[66]:


c.sort_values(ascending = False).head(5) # giảm dần


# In[68]:


# Unique value
df.item_name.value_counts()


# In[69]:


df.item_name.value_counts().count() # 50 món hàng khác nhau được bán ra


# In[70]:


df.item_name.nunique() # 50 món hàng khác nhau đc bán ra


# In[ ]:




