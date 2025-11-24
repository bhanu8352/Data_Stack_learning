import csv

with open("input_file.csv", 'r') as in_file:
    reader = csv.reader(in_file)

    with open ("op.csv", 'w') as op_file:
        writer = csv.writer(op_file)

        for line in reader:
            if Sex == "Female":
                print(line)




