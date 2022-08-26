# Toplululaştırma ve Gruplama( Aggregation & Grouping)
import pandas as pd
import seaborn as sns
pd.set_option('display.max.columns', None)
df = sns.load_dataset("titanic")
print(df.head())
# Yaşın ortalaması
a = df["age"].mean()
print(a)
b = df.groupby("sex")["age"].mean()
print(b)

#-------
c = df.groupby("sex").agg({"age": "mean"})
print(c)
d = df.groupby("sex").agg({"age": ["mean", "sum"]})
print(d)
e = df.groupby("sex").agg({"age": ["mean", "sum"],
                           "survived": "mean"})
print(e)
f = df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                                            "survived": "mean"})
print(f)
g = df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "sum"],
                                            "survived": "mean"})
print(g)
j = df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean", "sum"],
    "survived": "mean",
    "sex": "count"})
print(j)