import datetime
import pytz
myD=datetime.datetime(2020,9,9,11,0,0)
myD=pytz.UTC.localize(myD)
myD=myD.astimezone(pytz.timezone('US/Mountain'))


