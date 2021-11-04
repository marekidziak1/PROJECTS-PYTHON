import datetime

current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5
#First option
start_date = datetime.date.today()
days_to_lose=(current_weight-goal_weight)/avg_lbs_week*7
end_date = start_date + datetime.timedelta(days_to_lose)
print(f"The goal reached in {days_to_lose} at date: {end_date}")

#Second option
end_date=start_date
while current_weight>goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight-= avg_lbs_week
print(f"The goal reached in {end_date - start_date} at date: {end_date}")