# İloc & Loc Yapisi
# Dataframelerde seçim işlemi için kullanılan özel yapilardir.
# iloc = numpydan, listelerden integer bilgisi vererek seçim yapma işlemlerini ifade eder.
# loc = Mutlak olarak indexlerdeki labellara göre seçim yapar.
import pandas as pd
import seaborn as sns
pd.set_option('display.max.columns', None)
df = sns.load_dataset("titanic")
print(df.head())
# iloc: integer based selection
print(df.iloc[0:3])
#print(df.iloc[0, 0])
# loc : label based selection
print(df.loc[0:3])
#fark
a = df.iloc[0:3, 0:3]
b = df.loc[0:3, "age"]
print(a)
print(b)
# Birden fazla değişken isimlerini ifade ederek seçebiliriz.
col_names = ["age", "embarked", "alive"]
x = df.loc[0:3, col_names]
print(x)