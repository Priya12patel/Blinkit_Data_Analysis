import pandas as pd

df = pd.read_csv('BlinKIT Grocery Data.csv')
df.head()

df.shape

df.columns

df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head()

df = df.drop(['item_weight'],axis=1)
df.head()

df.info()

df.duplicated()

df['item_fat_content'].unique()

df['item_fat_content'].replace('LF','Low Fat',inplace=True)
df['item_fat_content'].replace('low fat','Low Fat',inplace=True)
df['item_fat_content'].replace('reg','Regular',inplace=True)

df['item_fat_content'].unique()

df['outlet_size'].unique()

df['outlet_location_type'].unique()

df.to_csv('BlinKIT_Grocery_Data1.csv')