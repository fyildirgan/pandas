import pandas as pd
import seaborn as sns
pd.set_option('display.max.columns', None)
df = sns.load_dataset("titanic")
print(df.head())
# 50'den büyük müdür sorgusu?
a = df[df["age"] > 50].head()
print(a)
# yasi 50den buyuk kac kısı var?
b = df[df["age"] > 50]["age"].count()
print(b)
c = df.loc[df["age"] > 50, "class"].head()
#print(c)
d = df[df["age"] > 50]["class"].head()
#print(d)
# print c ve d ayni islemi karsilamaktadir.
e = df.loc[df["age"] > 50, ["age", "class"]].head()
print(e)
# Ayni anda iki kosul girildiginde koseli parantez yerine
# normal parantez kullanilmasi gerekmektedir yoksa hata ile karsilasiriz.
f = df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
print(f)
g = df.loc[(df["age"] > 50)
           & (df["sex"] == "male")
           & (df["embark_town"] == "Cherbourg"),
           ["age", "class", "embark_town"]].head()
print(g)
print(df["embark_town"].value_counts())
h = df.loc[(df["age"] > 50)
           & (df["sex"] == "male")
           & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
           ["age", "class", "embark_town"]]
print(h)
h1 = df.loc[(df["age"] > 50)
           & (df["sex"] == "male")
           & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
           ["age", "class", "embark_town"]]
print(h1["embark_town"].value_counts())







