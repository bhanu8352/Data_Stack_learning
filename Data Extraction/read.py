import csv

#rows = []
with open("input_file.csv", 'r') as in_file:
    reader = csv.reader(in_file)

    with open ("op.csv", 'w') as op_file:
        writer = csv.writer(op_file)

    # fields = next(reader)
    for line in reader:
        #rows.append(line)
        top_five = line [:5]
        writer.writerow(top_five)

        print(top_five)




