import csv

file = "StudentsPerformance.csv"
output = "Mathscore_85.csv"

with open(file, 'r') as in_file:
    reader = csv.DictReader(in_file, delimiter=',') #reader objejct

    with open(output, 'w') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames) #writer object
        writer.writeheader()

        for list in reader:
            if int(list["math score"] )> 85 and list["gender"] == "female": #filter score >85 and gender female
                writer.writerow(list)
                print(list)