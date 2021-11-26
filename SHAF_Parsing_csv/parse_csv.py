import os 
os.chdir('2.Parsing_csv')
import csv

html_output=''
names=[]
with open('plik_csv.csv','r') as file:
    csv_reader=csv.reader(file)
    '''2 times next function to avoid header & unneeded values'''
    next(csv_reader)
    next(csv_reader)
    for line in csv_reader:
        if line[0]=='No Reward':
            break
        names.append(f'{line[0]}, {line[1]}')
html_output='<ul>\n'
for name in names:
    html_output+=f"\t<li>{name}</li>\n"
html_output+='</ul>\n'
print(html_output)


