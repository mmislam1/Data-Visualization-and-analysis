#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sb
import matplotlib as plt
import pandas as pd


df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Data visualization\Mother Jones - Mass Shootings Database, 1982 - 2023 - Sheet1.csv")


df[['city','state']]=df['location'].str.split(', ',expand=True)

print(df)


temp=df[['year','case']]
incidentsPerYear=temp.groupby('year',as_index=False).count()


print(incidentsPerYear)
sb.lineplot(data=incidentsPerYear, x='year',y='case').set(title='Incidents Per Year')


# In[4]:


temp=df[['state','case']]
shootingPerState=temp.groupby('state',as_index=False).count()


print(shootingPerState)
sb.set(rc = {'figure.figsize':(39,4)})
sb.barplot(data=shootingPerState, x='state',y='case').set(title='Incidents Per State')


# In[3]:


temp=df[['age_of_shooter','case']]
AgeOfShooter=temp.groupby('age_of_shooter',as_index=False).count()


print(AgeOfShooter)
sb.set(rc = {'figure.figsize':(39,4)})
sb.barplot(data=AgeOfShooter, x='age_of_shooter',y='case').set(title='Age Of Shooter')


# In[ ]:




