import pandas as pd

file = "StudentsPerformance.csv"
#output = "top_m.csv"
output = "t_m.xlsx"

reader = pd.read_csv(file) #read file

#get top scorer by subject 

top_math = reader[reader["math score"] == reader["math score"].max()]
print("Top Math Score: ")
print(top_math)

#top_math.to_csv("top_m.csv")
top_math.to_excel(output)
