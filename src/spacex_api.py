import pandas as pd

url: str = "https://api.spacexdata.com/v4/launches"

df = pd.read_json(url)

print(df.head())
print(df.columns)
print(df.dtypes)
