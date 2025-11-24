import pandas as pd
import matplotlib.pyplot as plt 

in_file = "data.csv"

df = pd.read_csv(in_file)

missing_dates = df[df["Date"].isna()]

df["Date"] = df["Date"].fillna(pd.Timestamp("2020-12-01"))

df["Date"] = pd.to_datetime(df["Date"],  errors = 'coerce')

print(df["Date"])


