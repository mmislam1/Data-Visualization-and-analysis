#!/usr/bin/env python
# coding: utf-8

# In[15]:


import seaborn as sb
import matplotlib as plt
import pandas as pd


df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Data visualization\Adult_Tobacco_Consumption_In_The_U.S.__2000-Present.csv",index_col=False)


print(df)




# In[32]:


lp=df[["Total Per Capita",'Year']]



sb.lineplot(x='Year',y='Total Per Capita',data=lp)


# In[29]:





# In[ ]:




