#!/usr/bin/env python
# coding: utf-8

# # TASK-1

# 1. Data Analysis with Pandas:
# Use the Pandas library to load a CSV file and perform basic data analysis
# tasks (e.g., finding the average of a column)

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv(r"C:\Users\mural\Downloads\Churn_Modelling (2).csv")
df.head()


# In[3]:


df.tail()


# In[4]:


df.shape


# In[5]:


df.size


# In[6]:


df.memory_usage()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.head()


# In[10]:


average_age = df['Age'].mean()
print(f"The average age is: {average_age}")


# In[11]:


unique_Geography = df['Geography'].unique()
print(unique_Geography)


# In[12]:


df.isnull().sum()


# In[13]:


df.columns


# In[14]:


columns_to_fill={'Geography','HasCrCard','IsActiveMember','Age'}
for column in df.columns:
    df[column]=df[column].fillna(df[column].mode()[0])


# In[15]:


df.isnull().sum()


# In[16]:


df.duplicated().sum()


# In[17]:


df=df.drop_duplicates()


# In[18]:


df.duplicated().sum()


# In[19]:


df.to_csv(r"C:\Users\mural\Downloads\Churn_Modelling (2).csv", index=False)


# In[ ]:




