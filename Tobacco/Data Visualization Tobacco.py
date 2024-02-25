#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sb
import matplotlib as plt
import pandas as pd


df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Data visualization\Data Visualization Tobacco\Adult_Tobacco_Consumption_In_The_U.S.__2000-Present.csv",index_col=False)


print(df)




# In[8]:


lp=df[["Total Per Capita",'Year']]

sb.set(rc = {'figure.figsize':(6,4)})
sb.lineplot(x='Year',y='Total Per Capita',data=lp).set(title='Line plot of Per capita Consumption')


# In[9]:


sb.regplot(x='Year',y='Total Per Capita',data=lp).set(title='Regression Plot of per capita Intake')


# In[10]:


temp=df[["Measure","Total Per Capita"]]


consumptionStyle=temp.groupby('Measure',as_index=False).sum()


print(consumptionStyle)
sb.barplot(data=consumptionStyle, x='Measure',y='Total Per Capita').set(title='Consumption Style')


# In[ ]:




