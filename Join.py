# Birlestirme ( Join ) Islemleri
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99
#Concat metodu bize dataframeleri birleştirmeye yarar.
print(pd.concat([df1, df2], ignore_index=True))
#print(pd.concat([df1, df2]))

# Merge İle Birleştirme Islemleri
df3 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})
df4 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})
print(df3)
print(df4)
#print(pd.merge(df3, df4))
print(pd.merge(df3, df4, on="employees"))
# Amaç: Her çalışanın müdürün bilgisine erişmek istiyoruz.
df5 = pd.merge(df3, df4)
df6 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})
print(df6)
print(pd.merge(df5, df6))

