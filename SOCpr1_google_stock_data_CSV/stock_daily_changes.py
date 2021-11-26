import csv
from datetime import datetime
path="stock_data.csv"
file=open(path, 'r', newline='')
reader=csv.reader(file)
header=next(reader)
data=[]
for row in reader:
    row[0]=datetime.strptime(row[0],'%m/%d/%Y')
    row[1]=float(row[1])
    row[2]=float(row[2])
    row[3]=float(row[3])
    row[4]=float(row[4])
    row[5]=int(row[5])
    row[6]=float(row[6])
    data.append(row)
file.close()
#print(data[0])
#WRITING:
returns_path="google_returns.csv"
file=open(returns_path, 'w')
writer=csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data)-1):
    row_today=data[i]
    date_today=row_today[0]
    price_today=row_today[-1]
    row_y=data[i+1]
    price_y=row_y[-1]
    daily_return=(price_today-price_y)/price_y
    date_today=date_today.strftime('%m/%d/%Y')
    writer.writerow([date_today, daily_return])
file.close()
