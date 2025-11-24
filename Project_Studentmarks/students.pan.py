import pandas as pd
import numpy as np

file = "StudentsPerformance.csv"

df = pd.read_csv(file)
#math_pass = df[df["math score"]>35] - to filter pass marks in math
#selected_columns = ["gender", "math score"] - fo filter the required colums 
out_file = df.to_excel("StudentsPerformnace.xlsx", sheet_name="studentsdata")

print(out_file.head())