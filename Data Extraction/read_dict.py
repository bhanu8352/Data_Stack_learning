import csv 

with open("input_file.csv", 'r') as in_file:
    reader = csv.DictReader(in_file)
    

    
    for line in reader:
        print(line)