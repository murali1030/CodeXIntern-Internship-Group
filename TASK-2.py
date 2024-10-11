#!/usr/bin/env python
# coding: utf-8

# # TASK-2

# 2. Data Visualization with Matplotlib and Seaborn:
# Load a dataset (e.g., from Kaggle) and create various visualizations (e.g.,
# bar charts, scatter plots, heatmaps) to analyze the data. Use Matplotlib
# and Seaborn for plotting and provide insights based on the visualizations.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\Users\mural\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.head()


# In[3]:


df.shape


# In[4]:


df.size


# In[5]:


df.memory_usage()


# In[6]:


df.describe()


# In[7]:


df.describe().T


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[10]:


df.duplicated().sum()


# In[11]:


df=df.drop_duplicates()


# In[12]:


df.head()


# In[13]:


df.columns


# In[18]:


df['PaymentMethod'].value_counts()


# In[19]:


df.gender.value_counts()


# In[20]:


df['Contract'].value_counts()


# In[21]:


plt.figure(figsize=(10,4))
sns.countplot(data=df,x='PaymentMethod')


# INSIGHTS:The graph shows the frequency of each payment method, highlighting the most and least preferred methods among customers.

# In[24]:


sns.histplot(data=df,x='Contract',kde=True)


# The graph shows the distribution of contract types, indicating which contract duration is most common among customers.

# In[25]:


df['gender'].value_counts().plot.pie(autopct='1%.1f%%')
plt.legend()


# The pie chart shows the gender distribution, highlighting the percentage of male and female customers in the dataset.

# In[26]:


sns.histplot(data=df,x='MonthlyCharges',kde=True,color='green')


# The graph shows the distribution of monthly charges, indicating the most common charge range and its spread among customers.
# 
# 
# 
# 
# 
# 
# 

# In[27]:


sns.countplot(data=df,x='MultipleLines')


# The graph displays the distribution of customers with or without multiple lines, highlighting the prevalence of each option.

# In[28]:


pd.crosstab(df['gender'],df['SeniorCitizen']).plot(kind='bar')


# The bar chart shows the distribution of senior and non-senior citizens across genders, revealing any differences in the proportion of senior citizens between males and females.
# 
# 
# 
# 
# 
# 
# 

# In[29]:


pd.crosstab(df['Contract'],df['DeviceProtection']).plot(kind='bar')


# The bar chart shows the relationship between contract types and device protection, highlighting which contract durations are more likely to include device protection.
# 
# 
# 
# 
# 
# 
# 

# In[30]:


pd.crosstab(df['Contract'],df['TechSupport']).plot(kind='bar')


# The bar chart illustrates the association between contract types and tech support, revealing the likelihood of customers opting for tech support based on their contract duration.
# 
# 
# 
# 
# 
# 
# 

# In[31]:


pd.crosstab(df['Contract'],df['StreamingTV']).plot(kind='bar')


# The bar chart shows the relationship between contract types and streaming TV subscriptions, indicating how contract duration influences the likelihood of subscribing to streaming TV services.
# 
# 
# 
# 
# 
# 
# 

# In[32]:


pd.crosstab(df['Contract'],df['StreamingMovies']).plot(kind='bar')


# 
# The bar chart illustrates the association between contract types and streaming movie subscriptions, highlighting trends in how contract duration affects the likelihood of subscribing to streaming movies.

# In[33]:


pd.crosstab(df['Contract'],df['PaymentMethod']).plot(kind='bar')


# The bar chart depicts the relationship between contract types and payment methods, revealing preferences for payment options based on contract duration.
# 
# 
# 
# 
# 
# 
# 

# In[36]:


pd.crosstab(df['Contract'],df['PaperlessBilling']).plot(kind='bar')


# The bar chart illustrates the relationship between contract types and paperless billing adoption, revealing how contract duration influences customers' preference for paperless billing.

# In[37]:


sns.scatterplot(data=df,x='MonthlyCharges',y='TotalCharges')


# 
# The scatter plot shows the relationship between monthly charges and total charges, indicating whether higher monthly fees correlate with increased total charges among customers.
# 
# 
# 
# 
# 
# 
# 

# In[39]:


sns.scatterplot(data=df,x='tenure',y='TotalCharges')


# The scatter plot shows the relationship between tenure and total charges, indicating that longer tenure is generally associated with higher total charges among customers.
# 
# 
# 
# 
# 
# 
# 

# In[40]:


sns.pairplot(df)


# The pair plot provides a comprehensive view of pairwise relationships between multiple variables in the dataset, revealing trends, correlations, and potential patterns among them.

# In[41]:


sns.heatmap(df.corr(),annot=True)


# The heatmap displays the correlation between multiple variables, highlighting the strength and direction of relationships, with annotated values indicating significant positive or negative correlations.

# In[ ]:




