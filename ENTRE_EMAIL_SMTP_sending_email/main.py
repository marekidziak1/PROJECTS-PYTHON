import sys
from formatting import format_msg
from send_mail import send_mail
def send(name, website=None, emails=None):
    if website==None:
        msg=format_msg(my_name=name)
    else:
        msg=format_msg(my_name=name, my_website=website) 
    #send message:
    send_mail(to_emails=emails, html=msg)
    
if __name__ =='__main__':
    emails=[]
    name=sys.argv[1]
    for i in range(2,len(sys.argv)):
        emails.append(sys.argv[i])
    send(name, None, emails)