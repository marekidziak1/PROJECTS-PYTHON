import os 
os.chdir('2.Parsing_csv')
import csv

html_output=''
names=[]
with open('plik_csv.csv','r') as file:
    csv_dict_reader=csv.DictReader(file)

    #next function to avoid unneeded values
    next(csv_dict_reader)
    for line in csv_dict_reader:
        
        if line['FirstName']=='No Reward':
            break
        #names.append('{}, {}'.format(line['FirstName'],line['Email']))
        a=line["FirstName"]
        b=line["Email"]
        names.append(f'{a}, {b}')
html_output='<ul>\n'
for name in names:
    html_output+=f"\t<li>{name}</li>\n"
html_output+='</ul>\n'
print(html_output)


