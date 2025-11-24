import csv 

with open("input_file.csv", 'r', newline='') as in_file:
    reader = csv.DictReader(in_file)

    with open("op_dict.csv", 'w', newline='') as op_file:
        writer = csv.DictWriter(op_file, fieldnames=reader.fieldnames)
        writer.writeheader()
    
        for line in reader:
            print(line)
            writer.writerow(line)
        
        