import csv
from email.message import EmailMessage
import ssl
import smtplib

sender = 'kush.vachher@gmail.com'
pw = 'asbq pxsw vfif zrmq'

subject = 'AUTOMATED ROOMMATE EMAIL'


def load_data(fname) : 
    mylist = []
    with open(fname) as data : 
        r = csv.reader(data)
        next(r) # skips header
        for row in r : 
            mylist.append(row)
        return mylist
    
new_list = load_data('roommates.csv')
for row in new_list :
    name = row[0]
    rec = row[1]
    if row[2] == "Yes" : 
        tall = True
    else : 
        tall = False
    body = f"Hi {name}! This is your roommate Kush Vachher. I'm emailing you to let you know that it is {tall} that you are 6 foot or over. Thanks for your time."

    em = EmailMessage()
    em['From'] = sender
    em['To'] = rec
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, pw)
        smtp.send_message(em)