import csv
file_name = "input_file.csv"
filter = ['First Name', 'Last Name', 'Sex', 'Email']

with open(file_name, 'r') as in_file:
    reader = csv.reader(in_file)

    with open("output.csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(filter)

        for row in reader:
            filtered_row = row [2:6]
            writer.writerow(filtered_row)

            print(filtered_row)

       
