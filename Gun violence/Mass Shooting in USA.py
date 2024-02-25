
import seaborn as sb
import matplotlib as plt
import pandas as pd


df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Data visualization\Mother Jones - Mass Shootings Database, 1982 - 2023 - Sheet1.csv")

df[['city','state']]=df['location'].str.split(', ',expand=True)

print(df)


temp=df[['year','case']]
consumptionStyle=temp.groupby('year',as_index=False).count()


print(consumptionStyle)
sb.barplot(data=consumptionStyle, x='year',y='case')
