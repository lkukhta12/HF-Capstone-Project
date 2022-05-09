#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv(r'\\Flws-ntxfs\cfr\lkukhta\Desktop\dataset files\Citywide_Payroll_Data__Fiscal_Year.csv')


# In[3]:


#looking thru the data 
df.head()


# In[4]:


#getting the count for rows
row_count = df.shape[0]
row_count


# In[5]:


#getting the count for columns
col_count = len(df.columns)
col_count


# In[6]:


#creating a new dataframe
df1 = df[['Fiscal Year','Agency Name', 'Work Location Borough', 'Title Description', 'Base Salary', 'Pay Basis']]


# In[7]:


df1.head()


# In[9]:


#dropping missing values
df1 = df1.dropna()


# In[10]:


#getting the count for rows after dropping na's
row_count = df1.shape[0]
row_count


# In[11]:


df1.to_csv(r'\\Flws-ntxfs\cfr\lkukhta\Desktop\NYCitywide_Payroll_Data.csv', index = False)


# In[ ]:




