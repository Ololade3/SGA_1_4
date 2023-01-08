#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import library
import sqlite3
#comfirming if packaged is sucessfully imported
print('Imported sucessfully')


# In[2]:


#connecting to database
connect = sqlite3.connect("attr_data.db")
#confirming if DB is created
print("connected to DB successfully", type(connect))


# In[3]:


#creating a cursor object
cursor = connect.cursor()
#confirming if the cursor object is creacted
print("cursor object created sucessfuly \n", type(cursor))


# In[4]:


#VIEW TABLES NAMES
query = """
SELECT name 
FROM sqlite_schema
WHERE type ='table';
"""
#excute query
cursor.execute(query)
#view result
query_result = cursor.fetchall()
query_result


# In[5]:


query = """
SELECT *
FROM sqlite_sequence
"""
#excute query
cursor.execute(query)
#view result
query_output = cursor.fetchall()
query_output


# In[6]:


#importing libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


#using pandas to view the table
query = """
SELECT *
FROM attrition_records
Limit 10;"""
cursor.execute(query)
df = pd.read_sql(query,connect)
df


# In[8]:


#DATA CLEANING
#Find number of missing values in every feature
df.isnull().sum()


# In[9]:


#Get list of columns in the dataset
df.columns


# In[10]:


#To get description of all columns
df.describe(include = 'all')


# In[11]:


df['Attrition'].value_counts()


# What do you think are the 3 factors behind employee attrition?

# In[24]:


#Finding correlation between variables
data_correlation = df.corr()
plt.rcParams["figure.figsize"] = [10,5]
sns.heatmap(data_correlation,xticklabels=data_correlation.columns,yticklabels=data_correlation.columns);


# # correlation results 
# Monthly income correlated with Job level.
# Job level is correlated with total working hours.
# Monthly income is correlated with total working hours.
# Age is also positively correlated with the Total working hours.
# Marital status and stock option level are negatively correlated

# In[25]:


fig, ax = plt.subplots(2,3,figsize=(18,10))
sns.countplot(x='BusinessTravel',data=df,ax=ax[0,0])
sns.countplot(x='Department',data=df,ax=ax[0,1])
sns.countplot(x='Education',data=df,ax=ax[0,2])
sns.countplot(x='EducationField',data=df,ax=ax[1,0])
sns.countplot(x='Gender',data=df,ax=ax[1,1])
sns.countplot(x='OverTime',data=df,ax=ax[1,2])
plt.title('General View of Data Distribution')
plt.tight_layout()


# In[13]:


#EDUCATION VS MONTHLY INCOME
#Does Monthly income effect employee attrition?
plt.figure(figsize=(10,5))
sns.boxplot(x=df["Education"],y=df["MonthlyIncome"])
plt.title("Education VS. Monthly Income");


# The income of employees depends on there level of Education.

# In[14]:


#What is the effect of age on attrition?
#Effect of age on attrition
#Plot to see distribution of age overall
plt.rcParams["figure.figsize"] = [7,7]
plt.hist(df['Age'], bins=np.arange(0,80,10), alpha=0.8, rwidth=0.9, color='blue');


# Result
# Employees whose age is in the range of 30 - 40 are more likely to quit.
# Employees in the range of 20 to 30 are also equally imposing the threat to employers.

# Is Income the main factor in employee attrition?
# 
# 

# In[15]:


sns.histplot(df['MonthlyIncome'], label='Negative attrition')
sns.histplot(df['MonthlyIncome'], label='positive attrition')
plt.legend();


# people who are less likely to leave the company are the ones who are less paid.

# In[17]:


##How does work-life balance impact the overall attrition rate?
pd.crosstab(columns=[df.Attrition],index=[df.WorkLifeBalance],margins=True,normalize='index') # set normalize=index to view rowwise %.


#  people with better work life balance dont want to leave the organisation.

# In[18]:


attr_balance = df.groupby(['WorkLifeBalance', 'Attrition']).apply(lambda x:x['DailyRate'].count()).reset_index(name='Count')
attr_balance.head()


# In[20]:


sns.set_style('whitegrid')
px.bar(data_frame=attr_balance,x='WorkLifeBalance',y='Count',color='Attrition',opacity=0.8)


# The worklife balance is seemingly having more attrition in higher range for the sole conquest of having much better life

# In[ ]:




