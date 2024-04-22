from email.message import EmailMessage
import ssl
import smtplib

recs = ['gvachher@gmail.com', 'nehavachher@yahoo.com', 'vachhertanya@gmail.com']

sender = 'kush.vachher@gmail.com'
pw = 'asbq pxsw vfif zrmq'

subject = 'HELLO TO MY FAMILY'
body = """
Hello to my wonderful family. I am currently learning how to send automatic emails with python. I hope 
this has reached you safely. Thank you for a fun weekend at home. 

Kush Vachher
"""

bcc_list = ", ".join(recs) 

em = EmailMessage()
em['From'] = sender
em['To'] = sender
em['Bcc'] = bcc_list 
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, pw)
    smtp.send_message(em)
