#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[37]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv(r'C:\Users\Dell\Desktop\datasets\winequality-red.csv')


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.shape


# In[7]:


df.isnull().sum()


# In[22]:


df.columns


# In[38]:


sns.countplot('quality', data=df)


# In[10]:


df["quality"].unique()


# In[11]:


sns.set_style("whitegrid")


# In[40]:


for features in df.columns:
    sns.scatterplot(x=df['quality'], y=df[features], data=df)
    plt.show();


# In[14]:


for features in df.columns:
    plt.hist(df[features])
    plt.xlabel(features)
    plt.show();


# In[46]:


corr_matrix=df.corr()
plt.figure(figsize=(16,8))
sns.heatmap(corr_matrix, annot=True)


# In[16]:


sns.pairplot(df)


# In[43]:


plt.figure(figsize=(10,5))
sns.barplot('quality', 'pH',data=df)


# In[44]:


plt.figure(figsize=(10,10))
sns.scatterplot('pH','alcohol', palette=['red','green','blue','orange','cyan','yellow'],hue='quality', data=df)


# In[45]:


fig,ax = plt.subplots(ncols = 6, nrows = 2,figsize = (20,10))
ax = ax.flatten()
index = 0
for col in df.columns:
    sns.distplot(df[col], ax = ax[index])
    index+=1


# In[ ]:




