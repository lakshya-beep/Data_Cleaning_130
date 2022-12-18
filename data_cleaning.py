import csv
import pandas as pd

df=pd.read_csv("merged.csv")

print(df.shape)

del df["lum"]
del df["star_name"]
del df["distance"]
del df["mass"]
del df["radius"]

df.to_csv("final.csv")