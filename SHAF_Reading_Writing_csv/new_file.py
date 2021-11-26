import os
os.chdir('practise')
import csv

with open('plik.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    with open('new_plik.csv','w')as new_csv_file:
        csv_writer=csv.writer(new_csv_file,delimiter='-')
        for line in csv_reader:
            csv_writer.writerow(line)
