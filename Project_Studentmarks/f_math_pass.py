import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("StudentsPerformance.csv")
filtered_data = df[["gender", "test preparation course"]]

math_pass = df[(df["math score"]<35)]
f_math_pass =  math_pass[math_pass["gender"] == "female"]

#rint(f_math_pass)
df["math score"].plot()
print(df.plot())
print(plt.show())