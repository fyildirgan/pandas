# Pandas Series

import pandas as pd
s = pd.Series([10, 77, 12, 4, 5])
print(s)
print(type(s))
print(s.index)
print(s.dtype)
print(s.size)
print(s.ndim)
print(s.values)
type(s.values)
print(s.head(3))
print(s.tail(3))