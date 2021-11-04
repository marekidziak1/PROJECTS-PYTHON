from formatting import format_msg
from datetime import datetime
import sys
import requests
def send(name, website=None):
    if website==None:
        msg=format_msg(my_name=name)
    else:
        msg=format_msg(my_name=name, my_website=website) 
    #send message:
    r=requests.get("http://httpbin.org/json")
    if r.status_code==200:
        return msg
    else:
        return r.json()
    
if __name__ =='__main__':
    new_name="Unknown"
    if len(sys.argv[1])>1:
        new_name=sys.argv[1]
    response= send(new_name)
    print(response)