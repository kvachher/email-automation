from email.message import EmailMessage
import ssl
import smtplib

sender = 'kush.vachher@gmail.com'
pw = 'asbq pxsw vfif zrmq'
rec = 'ogdesai@gmail.com'

subject = 'HELLO OM'
body = """
Hello to my dear friend Om. This email is being sent automatically with Python.
"""

em = EmailMessage()
em['From'] = sender
em['To'] = rec
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(sender, pw)
    smtp.sendmail(sender, rec, em.as_string())
