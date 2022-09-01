from email.message import EmailMessage
from app2 import password
import ssl
impprt smtplib

email_sender = 'coolestkhid40@gmail.com'
email_password = password

email_receiver = 'calebdogbe40@gmail.com'

subject = 'Dont forget to subscribe'
body = """ Hey, how are you doing"""

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())