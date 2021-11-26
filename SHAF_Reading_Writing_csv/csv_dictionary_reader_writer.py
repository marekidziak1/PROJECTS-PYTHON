import csv
import os
os.chdir('practise')
with open('plik.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    #for line in csv_reader:
    #    print(line)
    with open('slownik_csv_plik.csv','w') as new_csv_file:
        fieldnames=['first_name','last_name','email']
        csv_writer=csv.DictWriter(new_csv_file,fieldnames=fieldnames)
        csv_writer.writeheader()            #zapisuję pierwszy rząd z nazwami pól
        for line in csv_reader:             #bierze tylko wartosści ze słownika (bez kluczy)
            csv_writer.writerow(line)