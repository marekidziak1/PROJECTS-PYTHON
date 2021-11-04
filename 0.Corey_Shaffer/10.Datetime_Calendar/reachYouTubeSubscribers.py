import datetime
import math

goal_subs = 100_000
current_subs = 85_000
avg_subs_day = 200 
subs_to_go=goal_subs-current_subs
days_to_go=math.ceil(subs_to_go/avg_subs_day)

start_date = datetime.date.today()
print(f"End date when you reach the goal is: {start_date+datetime.timedelta(days=days_to_go)}")
