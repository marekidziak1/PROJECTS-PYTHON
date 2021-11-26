import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


username='antekmarek555@gmail.com'
password='pythonEntrepreneurs'

def send_mail(from_email="Od Antka <antekmarek555@gmail.com",text='Email Body', subject="Hello World", to_emails=None, html="<h1>My html text</h1>"):
    assert isinstance(to_emails, list)
    assert len(to_emails)>0
    #formatting mail	
    msg=MIMEMultipart('alternative')
    msg["From"]=from_email
    msg["To"]=", ".join(to_emails)
    msg["Subject"]=subject
    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)
    if html !=None:
        html_part=MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str=msg.as_string()
    #sending mail
    server=smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr=from_email,to_addrs=to_emails,msg=msg_str)
    server.quit()
#send_mail(to_emails=["antekmarek555@gmail.com"])
