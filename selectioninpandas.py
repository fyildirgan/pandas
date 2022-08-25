# Pandas'ta Seçim İşlemleri( Selection in Pandas)

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
print(df.index)
print(df[0:13])
print(df.drop(0, axis=0).head())
delete_indexes = [1, 3, 5, 7]
print(df.drop(delete_indexes, axis=0).head())
# Değişikliklerin kalici olmasini istiyorsak 2 yol var;
#df = df.drop(delete_indexes, axis=0)
#df.drop(delete_indexes, axis=0, inplace=True)

#Değişkeni İndexe Çevirmek
df["age"].head()
df.age.head()
df.index = df["age"]
#print(df.index)
#print(df.drop("age", axis=1).head())
#print(df.drop("age", axis=1, inplace=True))
# İndexi Değişkene Çevirmek
#df.index
#df["age"] = df.index
#print(df.head())

#df.reset_index().head()
df = df.reset_index().head()
df = df.reset_index()
print(df.head())







