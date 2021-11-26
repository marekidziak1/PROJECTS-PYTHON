import imaplib
import email

host="imap.gmail.com"
username='antekmarek555@gmail.com'
password='pythonEntrepreneurs'

def get_inbox():
    #connect and select inbox
    mail=imaplib.IMAP4_SSL(host=host)
    mail.login(username,password)
    mail.select("inbox")
    my_message=[]
    #download data
    #_, search_data=mail.search(None,'ALL')
    #_, search_data=mail.search(None,'UNSEEN')
    _, search_data=mail.search(None,'SEEN') #[b'4 5']
    for num in search_data[0].split():      #[b'4', b'5']
        email_data={}
        _, data=mail.fetch(num, '(RFC822)')
        _, b=data[0]
        email_message=email.message_from_bytes(b)
        for h in ['from', 'to', 'subject', 'date']:
            email_data[h]=email_message[h]
        for part in email_message.walk():
            if part.get_content_type()=='text/plain':
                body=part.get_payload(decode=True)
                email_data["body"]=body.decode()
            elif part.get_content_type()=='text/html':
                body=part.get_payload(decode=True)
                email_data["html_body"]=body.decode()
        my_message.append(email_data)
    mail.close()
    return(my_message)

if __name__=='__main__':
    for x in get_inbox(): 
        print(x)














host='imap.gmail.com'
username='antekmarek555@gmail.com'
password='pythonEntrepreneurs'

mail=imaplib.IMAP4_SSL(host)
mail.login(username,password)
mail.select("inbox")

connection_info, search_data=mail.search(None, 'UNSEEN')
for num in search_data[0].split():
    #downloading message from email:
    email_data = {}
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0] 
    #taking info from message:
