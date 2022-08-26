# Değişkenler Üzerine İşlemler
import pandas as pd
import seaborn as sns
pd.set_option('display.max.columns', None)
df = sns.load_dataset("titanic")
#print(df.head())

"age" in df
df["age"].head()
df.age.head()
#print(df["age"].head())
#print(type(df["age"].head()))
# Bir değişken seçerken sonucu seri ya da dataframe olarak
#alabiliriz, iki parantez girilmesi durumunda veri yapısı bozulmaz
#ve dataframe olmaya devam eder.
print(type(df[["age"]].head()))
# Birden fazla değişken seçmek için
print(df[["age", "alive"]])
col_names = ["age", "adult_male", "alive"]
print(df[col_names].head(5))
# Bir DataFrame' e değişken eklemek
a = df["age2"] = df["age"]**2
print(a.head(5))
b = df["age3"] = df["age"] / df["age2"]
print(b.head(5))
# Bir değişkeni silmek için 2 yol bulunmakta.
#print(df.drop("age3", axis=1).head())
print(df.drop(col_names, axis=1).head())
#Belirli bir string ifadeyi barındıran değişkenleri silmek istersek
print(df.loc[:, df.columns.str.contains("age")].head())
# ~ tilde işaretiyle bunun dışındakileri seç demiş oluruz.
print(df.loc[:, ~df.columns.str.contains("age")].head())
# loc. dataframelerde seçme işlemi olarak kullanılan bir yapıdır.







