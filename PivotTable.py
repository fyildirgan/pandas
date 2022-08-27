# Pivot Table
import pandas as pd
import seaborn as sns
pd.set_option('display.max.columns', None)
df = sns.load_dataset("titanic")
print(df.head())

a = df.pivot_table("survived", "sex", "embarked")
#print(a)
b = df.pivot_table("survived", "sex", "embarked", aggfunc="std")
#print(b)
c = df.pivot_table("survived", "sex", ["embarked", "class"])
#print(c)

d = df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
#print(d.head())
e = df.pivot_table("survived", "sex", ["new_age", "class"])
print(d)
print(e)
#pd.set_option('display.width', 500) bu kod bütün tabloyu yan yana
#görme imkanı sunar.


