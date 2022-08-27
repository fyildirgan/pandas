# Apply and Lambda
# Apply: Satır ya da sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar.
# Lambda: Bir fonksiyon tanımlama şeklidir.(tıpki def gibi)
# Farkı kullan at fonksiyonudur.
import pandas as pd
import seaborn as sns

pd.set_option('display.max.columns', None)
df = sns.load_dataset("titanic")
# pd.set_option('display.width', 500)
# print(df.head())
df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5
print(df.head())
print((df["age"] / 10).head())
print((df["age2"] / 10).head())
print((df["age3"] / 10).head())
# Old method
# for col in df.columns:
#    if "age" in col:
#        print(col)

# for col in df.columns:
#    if "age" in col:
#        print((df[col]/10).head())

# for col in df.columns:
#    if "age" in col:
#        df[col] = df[col]/10
# df.head()
# print(col)

p = df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()
print(p)
j = df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()
print(j)
v = df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()
print(v)


# Bu kadar karmaşık bir formul yazmak yerine su sekilde bir yol izleyebiliriz
def standard_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


print(df.loc[:, df.columns.str.contains("age")].apply(standard_scaler).head())
# Bütün yapılan değişiklikleri kaydetme:
#df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standard_scaler())
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standard_scaler)
print((df.head()))