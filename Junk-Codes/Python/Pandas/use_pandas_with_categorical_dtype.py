import pandas as pd

df = pd.DataFrame({"fruit": ["apple", "banana", "apple", "orange"]})
df["fruit"] = df["fruit"].astype("category")
print(df.dtypes)
