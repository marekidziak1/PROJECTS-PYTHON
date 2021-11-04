import datetime
import calendar

interest_rate = 14*.01
balance = int(input("Type how much money do you wanna take in a credit: "))
min_monthly_payment = (interest_rate/12) * balance+1
print(f"Min monthly payment: {min_monthly_payment}")
monthly_payment = round(float(input("Type how much money you wanna pay for month: ")),2)
while monthly_payment<= min_monthly_payment:
    print("you can't pay less than min monthly payment")
    monthly_payment = round(float(input("Type how much money you wanna pay for month: ")),2)
today = datetime.datetime.today()
#zwraca dzień od którego zaczyna się miesiąc (0=Monday, 1=Tuesday...) 
#oraz ilosc dni w miesiącu w danym roku
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month-today.day
first_next_month_date = today + datetime.timedelta(days=days_till_end_month+1)
new_month_date = first_next_month_date
all_interest_charges=0
months =0
while balance >0:
    interest_charge = (interest_rate/12) * balance
    balance += interest_charge
    balance -= monthly_payment

    all_interest_charges+=interest_charge
    months+=1

    balance=0 if balance <0 else round(balance,2)
    print(new_month_date, balance)

    days_in_current_month = calendar.monthrange(new_month_date.year, new_month_date.month)[1]
    new_month_date=new_month_date + datetime.timedelta(days=days_in_current_month)
print(f'''All interest charges you've paid are {round(all_interest_charges,2)} euro for {months} months''')

