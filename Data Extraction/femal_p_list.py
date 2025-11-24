import pandas as pd 

file = pd.read_csv("input_file.csv")

fem_list = file.loc[file["Sex"]=="Female", ["First Name", "Last Name", "Email", "Job Title"]]

fem_list.to_csv("femal_p_list.csv", index="False")

print(fem_list)