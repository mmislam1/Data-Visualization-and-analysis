
import seaborn as sb
import matplotlib as plt
import pandas as pd


df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Data visualization\Mother Jones - Mass Shootings Database, 1982 - 2023 - Sheet1.csv")

df[['city','state']]=df['location'].str.split(', ',expand=True)

print(df)


temp=df[['year','case']]
consumptionStyle=temp.groupby('year',as_index=False).count()


print(consumptionStyle)
sb.lineplot(data=consumptionStyle, x='year',y='case')


temp=df[['state','case']]
shootingPerState=temp.groupby('state',as_index=False).count()


print(shootingPerState)
sb.set(rc = {'figure.figsize':(39,4)})
sb.barplot(data=shootingPerState, x='state',y='case')
