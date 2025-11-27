import pandas as pd

in_file = "time_data.csv"

df = pd.read_csv(in_file, parse_dates=["Date"], index_col="Date")

print(df)